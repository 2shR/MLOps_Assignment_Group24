#!/bin/bash

# Stop old container
docker rm -f housing-api || true

# Pull latest image from Docker Hub
docker pull <your-docker-username>/housing-api:latest

# Run new container
docker run -d -p 5000:5000 --name housing-api <your-docker-username>/housing-api:latest
