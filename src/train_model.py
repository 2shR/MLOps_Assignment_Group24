# src/train_model.py
import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os


# Load data
X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")
y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()
y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()


def eval_and_log(model, name, params=None):
    with mlflow.start_run(run_name=name):
        mlflow.set_tag("mlflow.user", "Tushar Rastogi, Satyam Shukla, Prithviraj Pradhan, Shrabana Kumar")
        # Log parameters
        if params:
            mlflow.log_params(params)
        else:
            mlflow.log_param("model_type", name)

        # Train
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        # Metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)

        # Log model
        mlflow.sklearn.log_model(model, name="model")

        print(f"{name} - RMSE: {rmse:.3f}, R2: {r2:.3f}")


if __name__ == "__main__":
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:5000"
    os.environ["MLFLOW_EXPERIMENT_NAME"] = "California Housing Regression"
    os.environ["MLFLOW_ARTIFACT_ROOT"] = "/app/mlruns"
    mlflow.set_experiment("California Housing Regression")
    # Linear Regression
    lr_model = LinearRegression()
    eval_and_log(lr_model, "LinearRegression")
    # Decision Tree
    dt_model = DecisionTreeRegressor(max_depth=5)
    eval_and_log(dt_model, "DecisionTree", params={"max_depth": 5})
