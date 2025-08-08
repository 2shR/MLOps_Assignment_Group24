#!/bin/bash

# Stop old container
docker rm -f housing-api || true

# Pull latest image from Docker Hub
docker pull tusharrastogi/housing-api:latest

# Run new container
docker run -d -p 8080:8080 --name housing-api tusharrastogi/housing-api:latest
