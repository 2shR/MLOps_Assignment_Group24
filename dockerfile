# Use lightweight base image with Python
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY src/ ./src/

# Expose port
EXPOSE 8081

# Start the Flask app
CMD ["python", "src/api.py"]

ENV MLFLOW_TRACKING_URI=http://host.docker.internal:5000
