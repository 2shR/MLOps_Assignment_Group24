# Build the Docker image
docker build -t housing-api .

# Run the container
docker run -p 5000:5000 housing-api
