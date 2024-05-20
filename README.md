Steps to make airflow dag work

1. Set Up Your Environment

pip install apache-airflow
export AIRFLOW_HOME=~/airflow
airflow db init
airflow standalone


2.  Create Your DAG

Write your DAG file in Python and place it in the dags directory of your Airflow home.

Example: ~/airflow/dags/example_dag.py

copy the code from the example_Dag.py file and use it, as a example

3. Static Code Checks

pip install flake8
flake8 ~/airflow/dags/example_dag.py


4. Unit Testing Tasks

pip install pytest
Create a test file, e.g., test_example_dag.py: I have already created in repo just use it.

5. pytest test_example_dag.py


6. Manual DAG Trigger in Airflow UI

airflow webserver --port 8080

airflow scheduler


7. Testing Individual Tasks
airflow tasks test example_dag print_date 2023-01-01









