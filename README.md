# MLOps_Assignment_Group24
Group No 24 MLOps Assignment

+------------------+         +---------------------+         +--------------------+
|  Data Collection |  ---->  |  Data Preprocessing |  ---->  |  Model Training    |
| (Scikit-learn)   |         |  (Pandas, Scikit)   |         | (Linear, Tree + MLflow)
+------------------+         +---------------------+         +--------------------+
                                                                  |
                                                                  v
                                                         +-------------------+
                                                         | Experiment Tracking|
                                                         |     (MLflow)      |
                                                         +-------------------+
                                                                  |
                                                                  v
+---------------------+       +--------------------+     +--------------------+
|  REST API (Flask)   |<----->|  Docker Container   |<--->| GitHub Actions CI/CD|
+---------------------+       +--------------------+     +--------------------+
         |
         v
+----------------------+
| Monitoring & Logging |
| SQLite + Prometheus  |
+----------------------+
