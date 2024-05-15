# Evidently Metrics Deployment

This project contains a Python script that fetches metrics from various model endpoints and sends them to the Evidently service for evaluation. The script is containerized using Docker and deployed to a Kubernetes cluster.

## Prerequisites

-   Docker
-   Kubernetes cluster
-   kubectl command-line tool
-   Docker Hub account (or another container registry)

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

This project contains instructions for deploying a machine learning model using Seldon Core on a Kubernetes cluster. The model will be packaged in a Docker container and managed using Seldon Core.

## Prerequisites

-   Kubernetes cluster >= 1.23
-   Helm version >= 3.0
-   kubectl command-line tool
-   Docker Hub account (or another container registry)

## Step-by-Step Guide

### Step 1: Install Seldon Core

#### Install Helm 3.x

We have followed the instructions on the [Install Seldon core on Kubernetes](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/install.html#).

#### Install Seldon Core using Helm

1. We Add the Seldon Core Helm repo and update:

    ```bash
    helm repo add seldonio https://storage.googleapis.com/seldon-charts
    helm repo update
    ```

2. We Creates the `seldon-system` namespace:

    ```bash
    kubectl create namespace seldon-system
    ```

3. We Install Seldon Core in the `seldon-system` namespace with Istio enabled:

    ```bash
    helm install seldon-core seldonio/seldon-core-operator \
        --set usageMetrics.enabled=true \
        --set istio.enabled=true \
        --namespace seldon-system
    ```

### Step 2: Add to the Dockerfile for Our Model and deploy it
