from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime 
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


with DAG('dag_run_dag1', description='DAG RUN DAG 1 CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) as dag:

     task1 = BashOperator(task_id='task1', bash_command='sleep 5') 
     task2 = TriggerDagRunOperator(task_id='task2', trigger_dag_id='dag_run_dag2')
     
task1 >> task2 