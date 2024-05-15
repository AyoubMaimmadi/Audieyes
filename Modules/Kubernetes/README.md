# Evidently Metrics Deployment

This project contains a Python script that fetches metrics from various model endpoints and sends them to the Evidently service for evaluation. The script is containerized using Docker and deployed to a Kubernetes cluster.

## Prerequisites

- Docker
- Kubernetes cluster
- kubectl command-line tool
- Docker Hub account (or another container registry)

## Step-by-Step Guide

### Step 1: Create a Dockerfile

Create a Dockerfile to package your Python code. Save the following content into a file named `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "connect.py"]
```

### Step 2: Build and Push the Docker Image

```bash
docker build -t ayoubmaimmadi/evidently-metrics-fetcher .
docker push ayoubmaimmadi/evidently-metrics-fetcher
```

### Step 3: Create and run the Kubernetes Deployment

Please check the file [Kubernetes_Deployment](./evidently-deployment.yaml)

We run it using: kubectl apply -f evidently-metrics-fetcher-deployment.yaml


# Seldon Core Deployment

This contains instructions for deploying a machine learning model using Seldon Core on a Kubernetes cluster. The model will be packaged in a Kubernetes deployment.

## Prerequisites

- Kubernetes cluster
- kubectl command-line tool
- Seldon Core installed on Kubernetes cluster

### Step 1: Kubernetes deployment

Generate yaml deployment that is inherently connected with the model, please view: [Seldon_Core_Kubernetes_Deployment](./seldon-deployment.yaml)

and the apply it: kubectl apply -f seldon-deployment.yaml

