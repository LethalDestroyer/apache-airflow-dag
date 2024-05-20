from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator 

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG',
    schedule=timedelta(days=1),
)

task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

task2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag,
)

task3 = BashOperator(
    task_id='print_message',
    bash_command='echo "This is an additional stage"',
    dag=dag,
)

task1 >> task2 >> task3
