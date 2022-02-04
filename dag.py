
from airflow import models
from datetime import datetime, timedelta
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator

default_args = {
    'owner': 'Airflow',
    'start_date' : datetime(2021,12,28),
    'retries' : 1,
    'retry_delay': timedelta(seconds = 30),
    'dataflow_default-operations' : {
        'project':'consummate-yew-336502',
        'region':'us-central1',
        'runner':'DataFlowRunner'
    }
}

with models.DAG('food_order_dag',
    default_args = default_args,
    schedule_interval = "@daily",
    catchup=False) as dag:
    
    t1 = DataFlowPythonOperator(
    task_id = 'beamtask',
    py_file = 'gs://us-central1-demo-food-order-078c828f-bucket/updated_new.py',
    options = {'input' : 'gs://food-orders/food_daily.csv'}
    )