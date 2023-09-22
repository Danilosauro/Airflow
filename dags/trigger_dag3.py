from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime 

with DAG('trigger_dag3', description='DAG 7 CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) as dag:

     task1 = BashOperator(task_id='task1', bash_command='exit 1') 
     task2 = BashOperator(task_id='task2', bash_command='exit 1')
     task3 = BashOperator(task_id='task3', bash_command='sleep 5', 
     trigger_rule ='all_failed')

[task1, task2 ] >> task3