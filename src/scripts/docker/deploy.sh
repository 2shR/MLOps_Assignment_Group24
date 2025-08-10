#!/bin/bash

# Remove the old container
docker rm -f housing-api 

## OR stop the container
## docker stop housing-api

# Pull latest image from Docker Hub
docker pull tusharrastogi/housing-api:latest

# Run new container
docker run -d -p 8081:8081 --name housing-api tusharrastogi/housing-api:latest

# Check the status of container
docker ps