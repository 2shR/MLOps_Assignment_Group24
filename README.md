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

## Project Structure
mlops-california-housing/
├── .github/
│   └── workflows/
│       └── ci-cd.yml                  # GitHub Actions workflow for CI/CD
│
├── api/
│   ├── main.py                        # FastAPI app for model inference
│   ├── schemas.py                     # Pydantic models for input validation
│   ├── logger.py                      # Logging setup
│   ├── monitor.py                     # Prometheus metrics endpoint
│   └── retrain.py                     # Trigger model retraining on new data
│
├── data/
│   └── raw/
│       └── california_housing.csv     # Raw dataset (tracked via DVC, optional)
│
├── models/
│   └── model.pkl                      # Best trained model
│
├── notebooks/
│   └── eda.ipynb                      # Initial EDA and exploration
│
├── src/
│   ├── train.py                       # Model training and MLflow logging
│   ├── evaluate.py                    # Evaluate models
│   └── preprocess.py                  # Data preprocessing
│
├── Dockerfile                         # Dockerfile to containerize API
├── docker-compose.yml                 # Optional: for local multi-container setup
├── requirements.txt                   # Python dependencies
├── dvc.yaml                           # DVC pipeline (if used)
├── .dvc/                              # DVC internal metadata (if used)
├── README.md                          # Project README with run instructions
└── retrain_trigger.sh                 # Shell script to trigger retraining
