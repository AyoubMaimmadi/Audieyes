from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess
import mlflow

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dvc_to_mlflow_dag',
    default_args=default_args,
    description='Pull data from DVC and push to MLflow',
    schedule_interval=timedelta(days=1),
)

def dvc_pull():
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/gdrive://1T8YRTl9hhN5CZDh_dtEKoTnDI-qaHXCK"
    subprocess.run(["dvc", "pull"], check=True)

def push_to_mlflow():
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("DVC to MLflow")

    with mlflow.start_run():
        # Log a parameter (key-value pair)
        mlflow.log_param("param1", 5)

        # Log a metric; metrics can be updated throughout the run
        mlflow.log_metric("foo", 1)
        mlflow.log_metric("foo", 2)
        mlflow.log_metric("foo", 3)

        # Log an artifact (output file)
        with open("output.txt", "w") as f:
            f.write("Hello world!")
        mlflow.log_artifact("output.txt")

with dag:
    dvc_pull_task = PythonOperator(
        task_id='dvc_pull_task',
        python_callable=dvc_pull,
    )

    push_to_mlflow_task = PythonOperator(
        task_id='push_to_mlflow_task',
        python_callable=push_to_mlflow,
    )

    dvc_pull_task >> push_to_mlflow_task
