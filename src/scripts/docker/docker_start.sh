# Build the Docker image
docker build -t tusharrastogi/housing-api:latest .
docker run -p 8081:8081 -v E:/Assignment/MLOps_Assignment_Group24/mlruns:/app/mlruns housing-api
