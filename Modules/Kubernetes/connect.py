import requests

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

endpoints = {
    "model_1": "http://10.2.0.131:80/metrics",
    "model_2": "http://10.2.0.132:80/metrics",
    "model_3": "http://10.2.0.5:80/metrics",
    "model_4": "http://10.2.0.135:80/metrics",
    "model_5": "http://10.2.0.136:80/metrics",
}

# Fetch metrics and send to Evidently
for model_name, endpoint in endpoints.items():
    metrics = fetch_metrics_from_endpoint(endpoint)
    if metrics:
        send_metrics_to_evidently(metrics, model_name)

# Evaluate models based on user feedback and determine the best one
evaluation_results = evaluate_models_with_evidently()
if evaluation_results:
    best_model = max(evaluation_results, key=lambda x: x["user_feedback_score"])
    best_model_endpoint = endpoints[best_model["model_name"]]
    print(f"The best model based on user feedback is {best_model['model_name']} with endpoint {best_model_endpoint}")
