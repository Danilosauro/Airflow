from airflow import DAG
from airflow.operators.bash import BashOperator 
from airflow.operators.empty import EmptyOperator


from datetime import datetime 

with DAG('exemplo_empty', description='DUMMY CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) as dag:

     task1 = BashOperator(task_id='tsk1', bash_command='sleep 1') 
     task2 = BashOperator(task_id='tsk2', bash_command='sleep 1')
     task3 = BashOperator(task_id='tsk3', bash_command='sleep 1')
     task4 = BashOperator(task_id='tsk4', bash_command='sleep 1')
     task5 = BashOperator(task_id='tsk5', bash_command='sleep 1') 
     task_empty = EmptyOperator(task_id='task_empty')
     
[task1, task2, task3] >> task_empty >> [task4, task5]