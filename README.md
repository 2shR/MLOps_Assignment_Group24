# MLOps_Assignment_Group24
Group No 24 MLOps Assignment

# End-to-End MLOps Pipeline – California Housing

An end-to-end MLOps pipeline built using the California Housing dataset. This project demonstrates full lifecycle:
- Data preprocessing
- Model training & tracking
- CI/CD deployment
- Docker packaging
- Real-time monitoring & logging
- Model retraining automation

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
✅ Prometheus monitoring  
✅ Retraining on new data  

---

<pre>

mlops-california-housing/
├── .github/
│   └── workflows/
│       └── ci-cd.yml               # GitHub Actions for CI/CD
│
├── api/
│   ├── main.py                     # FastAPI app for serving model predictions
│   ├── schemas.py                  # Pydantic models for input validation
│   ├── logger.py                   # Logging of requests/responses
│   ├── monitor.py                  # Prometheus metrics endpoint
│   └── retrain.py                  # Retraining logic triggered via endpoint
│
├── data/
│   └── raw/
│       └── california_housing.csv  # Raw dataset (versioned with DVC if enabled)
│
├── models/
│   └── model.pkl                   # Trained & selected best model
│
├── notebooks/
│   └── eda.ipynb                   # Initial EDA and visualization
│
├── src/
│   ├── train.py                    # Training script with MLflow logging
│   ├── evaluate.py                 # Evaluate trained models
│   └── preprocess.py               # Data preprocessing utilities
│
├── Dockerfile                     # Dockerfile for API service
├── docker-compose.yml             # Optional: multi-container setup
├── requirements.txt               # Python dependencies
├── dvc.yaml                       # DVC pipeline file (if using DVC)
├── .dvc/                          # DVC metadata
├── retrain_trigger.sh             # Script to trigger retraining
└── README.md                      # Project overview and setup instructions

</pre>
---
