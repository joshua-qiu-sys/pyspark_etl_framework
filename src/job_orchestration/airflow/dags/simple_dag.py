from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os
from data_pipeline_app.ingestion.main import ingest

dag_id = os.path.basename(__file__).replace('.py', '')
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

def run_python_script():
    print('hello_world')

with DAG(dag_id=dag_id,
         default_args=default_args):
    
    simple_task = PythonOperator(task_id='simple_task',
                                 python_callable=run_python_script)
    
    simple_task