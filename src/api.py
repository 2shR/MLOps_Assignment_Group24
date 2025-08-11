from pydantic import BaseModel
from flask import Flask, request, jsonify
import mlflow
import pandas as pd
import traceback
import time
import sqlite3
import logging
from mlflow.tracking import MlflowClient
import mlflow.pyfunc
import os


# Define the input schema using Pydantic
class HousingInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


logging.basicConfig(filename='api.log', level=logging.INFO)
mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://host.docker.internal:5000")
)

# Load the MLflow model
MODEL_NAME = "BestCaliforniaHousingModel"
client = MlflowClient()
app = Flask(__name__)
latest_version = client.get_latest_versions(MODEL_NAME)[0].version

model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/{latest_version}")

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
    print(start_time)
    try:
        input_json = request.get_json()
        # Input fields validation
        validated = HousingInput(**input_json)
        input_df = pd.DataFrame([validated.dict()])
        prediction = model.predict(input_df)
        latency = (time.time() - start_time) * 1000
        # Logging to file
        logging.info(
            f"Request: {input_json} | Prediction: {prediction.tolist()} | "
            f"Latency: {latency} ms"
        )
        # Logging to SQLite
        # Logging to SQLite
        cursor.execute(
            "INSERT INTO logs (timestamp, input_json, prediction, latency_ms) "
            "VALUES (datetime('now'), ?, ?, ?)",
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

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is up and running!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
