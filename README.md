# MLOps_Assignment_Group24
Group No 24 MLOps Assignment:
| S.No | Name | BITS ID | Contribution |
|------|------|------|------|
| 1 | Tushar Rastogi | 2023AC05786 | 100% |
| 2 | Satyam Shukla | 2023AC05822 | 100% |
| 3 | Prithviraj Pradhan | 2023AC05770 | 100% |
| 4 | Shrabana Kumar | 2023AC05033 | 100% |

# End-to-End MLOps Pipeline – California Housing

An end-to-end MLOps pipeline built using the California Housing dataset. This project demonstrates full lifecycle:
- Data preprocessing
- Model training & tracking
- CI/CD deployment
- Docker packaging
- Real-time monitoring & logging

---

## Features

✅ Data preprocessing  
✅ Model training (Linear, Tree)  
✅ Experiment tracking with MLflow  
✅ Model Registry  
✅ Flask API with Pydantic validation  
✅ Dockerized  
✅ GitHub Actions for CI/CD  
✅ SQLite logging  

---

<pre>

```
MLOps_Assignment_Group24/
├── src/
│   ├── scripts/
│   │   └── docker/
│   │   │   ├── deploy.sh
│   │   │   ├── docker_start.sh
│   │   │   ├── docker-push.sh
│   │   │   └── start_deploy.sh
│   │   └── flake8/
│   │   │   └── run_flake8_analysis.sh
│   │   └── init_setup/
│   │   │   └── initial_dvc_setup.sh
│   │   └── logs/
│   │   │   └── check_logs.sh
│   │   └── mlflow/
│   │   │   └── mlflow.sh
│   │   └── tests/
│   │       └── run_tests.sh
│   ├── api.py
│   ├── data_prep.py
│   ├── train_model.py
│   ├── register_model.py
│   └── __init__.py
├── data/
│   └── processed/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
├── tests/
│   ├── api_test.py
│   ├── register_model_test.py
│   └── train_model_test.py
├── .github/
│   └── workflows/
│       ├── ci-cd.yml
│       └── .flake8
├── mlruns ├── ... # MLFlow Runs
├── mlartifacts ├── ... # MLFlow Model Artifacts
├── requirements.txt
├── requirements-dev.txt
├── dockerfile
├── logs.db
├── mlflow.db
├── README.md
└── .gitignore
```
</pre>
---

## 🔶 Architecture Overview

The project follows an **end-to-end MLOps pipeline** for the California Housing dataset, covering model development, deployment, and monitoring.

### **1. Repository and Data Versioning**
- **Dataset**: California Housing dataset.
- **Data Versioning**: Using DVC, data versioning is achieved and only pushed lightweight dvc files instead of actual datasets.
- **Directory Structure**: Shown above

### **2. Model Development & Experiment Tracking**
- **Model Training**: Uses `scikit-learn` for training linear regression and decision tree models.
- **Experiment Tracking**: Managed using **MLflow** with locally saved `mlflow.db` using sqlite.
- **Model Registry**: Registering best performing model for predictions.

### **3. API & Docker Packaging**
- **API Framework**: Flask-based REST API.
- **Validation**: Input validation using pydantic
- **Containerization**: Docker used to package the app and model.
- **Port Mapping**: Application exposed at `http://localhost:8081`.

### **4. CI/CD with GitHub Actions**
- **Lint Analysis**: Using `flake8` code analysis
- **GitHub Actions**: Automates testing, building, and pushing Docker images to Docker Hub.

### **5. Logging and Monitoring**
- **Logging**: Logging all the requests and output for Predict endpoint.
- **Application Metrics**: All the metrics of the application are logged and can be viewed under /metrics endpoint.
- **Persisting Logs**: Persisting all the logs to `file` and sqlite locally stored db `logs.db`

### **6. Pipeline Workflow**
```mermaid
flowchart TD
    A[Data Source: California Housing] --> B[Data Preprocessing]
    B --> C[Model Training & Hyperparameter Tuning]
    C --> D[MLflow Tracking & Model Registry]
    D --> E[Dockerized Flask API]
    E --> F[Deployment: Local/Docker Hub]

