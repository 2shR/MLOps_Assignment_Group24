# Stop and remove the existing container if it exists
docker stop housing-api -ErrorAction SilentlyContinue
docker rm housing-api -ErrorAction SilentlyContinue

# Pull latest image from Docker Hub
docker pull tusharrastogi/housing-api:latest

# Run new container
docker run -d -p 8081:8081 --name housing-api tusharrastogi/housing-api:latest

Write-Host "Deployment complete! API should be accessible at http://localhost:8081/predict"