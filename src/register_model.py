# src/register_model.py

import mlflow

# Set the MLflow tracking URI to match your MLflow server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

experiment_name = "California Housing Regression"
model_name = "BestCaliforniaHousingModel"

client = mlflow.tracking.MlflowClient()
experiment = client.get_experiment_by_name(experiment_name)
runs = client.search_runs(experiment.experiment_id, 
                        order_by=["metrics.rmse ASC"])

# Best run (lowest RMSE)
best_run = runs[0]
run_id = best_run.info.run_id

# Register model
model_uri = f"runs:/{run_id}/model"
result = mlflow.register_model(model_uri=model_uri, name=model_name)

print(f"Registered model from run {run_id}")
