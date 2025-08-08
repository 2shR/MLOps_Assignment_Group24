# Build the Docker image
docker build -t housing-api .

# Run the container
docker run -p 8080:8080 housing-api

# OR


 docker run -p 8081:8081 -v E:/Assignment/MLOps_Assignment_Group24/mlruns:/app/mlruns housing-api
