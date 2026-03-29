from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="create_dummy_file",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    description="Cria um arquivo .dummy usando BashOperator",
) as dag:
    create_dummy = BashOperator(
        task_id="create_dummy_file",
        bash_command="touch /opt/airflow/dags/.dummy"
    )