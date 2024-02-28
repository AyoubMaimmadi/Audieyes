import mlflow
import torch
from mlflow import pytorch

# Model checkpoints and their configurations
models = {
    "model_base": {"path": "model_base.pth", "model_size": "base", "pretraining_dataset": "ImageNet"},
    "model_base_retrieval_flickr": {"path": "model_base_retrieval_flickr.pth", "model_size": "base", "pretraining_dataset": "Flickr"},
    "model_vqa": {"path": "model_vqa.pth", "model_size": "base", "pretraining_dataset": "VQA"},
    "model_base_nlvr": {"path": "model_base_nlvr.pth", "model_size": "base", "pretraining_dataset": "NLVR2"},
    "model_base_retrieval_coco": {"path": "model_base_retrieval_coco.pth", "model_size": "base", "pretraining_dataset": "COCO"},
}

# Initialize MLflow tracking
mlflow.set_experiment("BLIP_Model_Comparison")

for model_name, model_info in models.items():
    with mlflow.start_run(run_name=model_name):
        # Load the model
        # model = torch.load(model_info["path"], map_location=torch.device('cpu'))
        model = torch.load(model_info["path"])
        
        # Log the model
        mlflow.pytorch.log_model(model, model_name)
        
        # Log parameters
        mlflow.log_param("model_size", model_info["model_size"])
        mlflow.log_param("pretraining_dataset", model_info["pretraining_dataset"])
        
        # Example generic metrics (these should be replaced with actual evaluation results)
        if "retrieval" in model_name:
            mlflow.log_metric("recall@1", 0.7)  # recall@1: retrieval performance
            mlflow.log_metric("recall@5", 0.8)  # recall@5: retrieval performance
        elif "vqa" in model_name:
            mlflow.log_metric("vqa_accuracy", 0.65)  # VQA accuracy
        elif "nlvr" in model_name:
            mlflow.log_metric("nlvr2_accuracy", 0.75)  # NLVR2 accuracy
        else:
            mlflow.log_metric("accuracy", 0.85)  # accuracy for base model
            mlflow.log_metric("loss", 0.2)  
        
        mlflow.end_run()
