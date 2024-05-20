import pytest
from airflow.models import DagBag

def test_dag_integrity():
    dag_bag = DagBag(dag_folder='/Users/shubhharne/airflow/dags', include_examples=False)
    assert 'example_dag' in dag_bag.dags
    assert len(dag_bag.import_errors) == 0, dag_bag.import_errors

if __name__ == '__main__':
    pytest.main()
