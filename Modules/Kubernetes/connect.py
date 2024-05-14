import requests

def send_metrics_to_evidently(metrics):
    url = "http://evidently-service.default.svc.cluster.local:5000/metrics"
    response = requests.post(url, json=metrics)
    if response.status_code == 200:
        print("Metrics sent successfully.")
    else:
        print("Failed to send metrics. Status code:", response.status_code)

metrics = {
    "TR@1": 0.85,     # Text Retrieval at 1
    "IR@1": 0.90,     # Image Retrieval at 1
    "TR@5": 0.92,     # Text Retrieval at 5
    "IR@5": 0.88,     # Image Retrieval at 5
    "TR@10": 0.95,    # Text Retrieval at 10
    "IR@10": 0.93,    # Image Retrieval at 10
    "B@4": 0.75,      # BLEU-4 Score
    "CIDEr": 1.02,    # Consensus-based Image Description Evaluation
    "SPICE": 0.65     # Semantic Propositional Image Caption Evaluation
}

send_metrics_to_evidently(metrics)
