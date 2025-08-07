# src/api.py

from flask import Flask, request, jsonify
import mlflow
import pandas as pd
import traceback
import time
import sqlite3
import logging


logging.basicConfig(filename='api.log', level=logging.INFO)


app = Flask(__name__)

# Load the MLflow model
MODEL_NAME = "BestCaliforniaHousingModel"
model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/Production")

# Connect to SQLite DB (local file)
conn = sqlite3.connect("logs.db", check_same_thread=False)
cursor = conn.cursor()

# Create table to log requests
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        input_json TEXT,
        prediction TEXT,
        latency_ms REAL
    )
''')
conn.commit()


@app.route("/predict", methods=["POST"])
def predict():
    start_time = time.time()
    try:
        input_json = request.get_json()
        input_df = pd.DataFrame([input_json])
        prediction = model.predict(input_df)
        latency = (time.time() - start_time) * 1000
		# Logging to log file
        logging.info(f"Request: {input_json} | Prediction: {prediction.tolist()} | Latency: {latency} ms")
        # Logging to SQLite
        cursor.execute(
            "INSERT INTO logs (timestamp, input_json, prediction, latency_ms) VALUES (datetime('now'), ?, ?, ?)",
            (str(input_json), str(prediction.tolist()), latency)
        )
        conn.commit()

        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        })


@app.route("/metrics", methods=["GET"])
def metrics():
    cursor.execute("SELECT COUNT(*), AVG(latency_ms) FROM logs")
    result = cursor.fetchone()
    return jsonify({
        "total_predictions": result[0],
        "average_latency_ms": round(result[1], 2) if result[1] else None
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
