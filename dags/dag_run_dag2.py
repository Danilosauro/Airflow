from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime 

with DAG('dag_run_dag2', description='DAG RUN DAG 2 CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) as dag:

     task1 = BashOperator(task_id='task1', bash_command='sleep 5') 
     task2 = BashOperator(task_id='task2', bash_command='sleep 5')
     
task1 >> task2 