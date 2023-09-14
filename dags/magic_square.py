from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime 

dag= DAG('magic_saquare', description='magic square DAG CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) 

task1 = BashOperator(task_id='Ronaldinho', bash_command='echo showman', dag=dag) 
task2 = BashOperator(task_id='Kaká', bash_command='echo arrancada', dag=dag)
task3 = BashOperator(task_id='Adriano', bash_command='echo o tanque', dag=dag) 
task4 = BashOperator(task_id='Ronaldo', bash_command='echo balanca e e gol', dag=dag)

[task1, task2, task3] >> task4 