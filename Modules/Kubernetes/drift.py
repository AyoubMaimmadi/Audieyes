import requests
import json

# Function to fetch metrics from an endpoint
def fetch_metrics_from_endpoint(endpoint):
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()  
        else:
            print(f"Failed to fetch metrics from {endpoint}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching metrics from {endpoint}: {e}")
        return None

# Function to send metrics to Evidently
def send_metrics_to_evidently(metrics, model_name):
    url = "http://evidently-service.default.svc.cluster.local:5000/metrics"
    data = {
        "model_name": model_name,
        "metrics": metrics
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Metrics sent successfully for {model_name}.")
        else:
            print(f"Failed to send metrics for {model_name}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending metrics to Evidently: {e}")

# Function to evaluate models with Evidently
def evaluate_models_with_evidently():
    url = "http://evidently-service.default.svc.cluster.local:5000/evaluate"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json() 
        else:
            print(f"Failed to evaluate models. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error evaluating models with Evidently: {e}")
        return None

# Function to introduce noise into the dataset for drift detection
def add_noise_to_dataset(dataset):
    noisy_dataset = []
    for item in dataset:
        noisy_captions = [caption + " noise" for caption in item['caption']]
        noisy_item = item.copy()
        noisy_item['caption'] = noisy_captions
        noisy_dataset.append(noisy_item)
    return noisy_dataset

# dataset
data_url = "https://storage.googleapis.com/sfr-vision-language-research/datasets/flickr30k_test.json"
dataset = requests.get(data_url).json()

# Add noise to dataset to simulate data drift
noisy_dataset = add_noise_to_dataset(dataset)

# Example function to simulate getting metrics from a model
def get_model_metrics(dataset):
    # This is a mock function. Replace with actual model inference and metric calculation.
    return {
        "accuracy": 0.85 if dataset == noisy_dataset else 0.95,  
        "response_time": 120,
        "system_throughput": 1000
    }

# List of model endpoints (mocked for this example)
endpoints = {
    "model_1": "http://10.2.0.131:80/metrics",
    "model_2": "http://10.2.0.132:80/metrics",
    "model_3": "http://10.2.0.5:80/metrics",
    "model_4": "http://10.2.0.135:80/metrics",
    "model_5": "http://10.2.0.136:80/metrics",
}

# Fetch metrics and send to Evidently
for model_name, endpoint in endpoints.items():
    metrics = get_model_metrics(dataset)  # Replace this with fetch_metrics_from_endpoint(endpoint) for actual use
    if metrics:
        send_metrics_to_evidently(metrics, model_name)
    noisy_metrics = get_model_metrics(noisy_dataset)
    if noisy_metrics:
        send_metrics_to_evidently(noisy_metrics, model_name + "_noisy")

# Evaluate models and detect drift
evaluation_results = evaluate_models_with_evidently()
if evaluation_results:
    best_model = max(evaluation_results, key=lambda x: x["accuracy"])
    print(f"The best model based on user feedback is {best_model['model_name']}")
    # Check for drift by comparing performance on noisy dataset
    drift_detected = any(result for result in evaluation_results if result['model_name'].endswith('_noisy') and result['accuracy'] < 0.9)
    if drift_detected:
        print("Data drift detected. Performance has dropped on the noisy dataset.")
