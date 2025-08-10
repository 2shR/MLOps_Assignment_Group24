import mlflow

def test_mlflow_tracking_uri():
    uri = mlflow.get_tracking_uri()
    assert uri.startswith("http")