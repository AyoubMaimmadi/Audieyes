import mlflow
import os

def train_model(learning_rate, batch_size):
    # Start MLflow run
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("batch_size", batch_size)
        # Log metrics individually
        accuracy = 0.88
        loss = 0.3
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("loss", loss)

        metrics = {
            "tr1": 0.82, # Text Retrieval @1
            "ir1": 0.65, # Image Retrieval @1
            "tr5": 0.96, # Text Retrieval @5
            "ir5": 0.87, # Image Retrieval @5
            "tr10": 0.97, # Text Retrieval @10
            "ir10": 0.91, # Image Retrieval @10
            "b4": 40.0, # BLEU Score
            "cider": 136.7, # CIDEr Score
            "spice": 14.8, # SPICE Score
        }

        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(metric_name, metric_value)

        # Log dataset configuration as an artifact
        dataset_config_path = "C:/Users/Ayoub Maimmadi/Documents/AUI/Asmae Mourhir/Audieyes/Audieyes/data/retrieval_coco.yaml"
        if os.path.exists(dataset_config_path):
            mlflow.log_artifact(dataset_config_path, "dataset_config")
        else:
            print("Dataset configuration file not found at specified path:", dataset_config_path)
        
        # Log model file as an artifact
        model_path = "C:/Users/Ayoub Maimmadi/Documents/AUI/Asmae Mourhir/Audieyes/Audieyes/models\model_base_retrieval_coco.pth"
        if os.path.exists(model_path):
            mlflow.log_artifact(model_path, "model_checkpoint")
        else:
            print("Model file not found at specified path:", model_path)



if __name__ == "__main__":
    # Define hyperparameters
    learning_rate = 0.01
    batch_size = 32

    # Call train_model function
    train_model(learning_rate, batch_size)
