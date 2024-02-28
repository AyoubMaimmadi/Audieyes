import mlflow
import os

def train_model(learning_rate, batch_size):
    # Start MLflow run
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("batch_size", batch_size)

        # Log dataset configuration as an artifact
        dataset_config_path = "C:/Users/Ayoub Maimmadi/Documents/AUI/Asmae Mourhir/Audieyes/Audieyes/configs/pretrain.yaml"
        if os.path.exists(dataset_config_path):
            mlflow.log_artifact(dataset_config_path, "dataset_config")
        else:
            print("Dataset configuration file not found at specified path:", dataset_config_path)
        
        # Log model file as an artifact
        model_path = "C:/Users/Ayoub Maimmadi/Documents/AUI/Asmae Mourhir/Audieyes/Audieyes/models/model_base.pth"
        if os.path.exists(model_path):
            mlflow.log_artifact(model_path, "model_checkpoint")
        else:
            print("Model file not found at specified path:", model_path)

        # Simulate retrieving metrics from paper and log them
        # These values should be replaced with the actual values obtained from the model's evaluation
        metrics = {
            "TR@1": 0.80, # Text Retrieval @1
            "IR@1": 0.63, # Image Retrieval @1
            "TR@5": 0.95, # Text Retrieval @5
            "IR@5": 0.85, # Image Retrieval @5
            "TR@10": 0.97, # Text Retrieval @10
            "IR@10": 0.91, # Image Retrieval @10
            "B@4": 38.0, # BLEU Score
            "CIDEr": 127.8, # CIDEr Score
            "SPICE": 13.9, # SPICE Score
        }

        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(metric_name, metric_value)

        # Since actual training and evaluation isn't included in this script,
        # the metrics above are placeholders for the real evaluation results.
        # Replace them with actual evaluation results from the model checkpoint.

if __name__ == "__main__":
    # Define hyperparameters
    learning_rate = 0.01
    batch_size = 32

    # Call train_model function
    train_model(learning_rate, batch_size)
