# src/api.py

from flask import Flask, request, jsonify
import mlflow
import pandas as pd
import traceback

app = Flask(__name__)

# Load registered model
MODEL_NAME = "BestCaliforniaHousingModel"
model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/Production")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON input
        input_json = request.get_json()

        # Convert to DataFrame
        input_df = pd.DataFrame([input_json])

        # Predict
        prediction = model.predict(input_df)

        return jsonify({"prediction": prediction.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e), "trace": traceback.format_exc()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
