import mlflow

def train_model(learning_rate, batch_size):
    # Start MLflow run
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("batch_size", batch_size)

        # Simulate training and log metrics
        accuracy = 0.85
        loss = 0.3
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("loss", loss)

        # Log artifacts (e.g., model file)
        # mlflow.log_artifact("model.pkl")

if __name__ == "__main__":
    # Define hyperparameters
    learning_rate = 0.01
    batch_size = 32

    # Call train_model function
    train_model(learning_rate, batch_size)
