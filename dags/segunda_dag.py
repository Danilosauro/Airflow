from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime 

dag= DAG('segunda_dag', description='DAG 2 CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) 

task1 = BashOperator(task_id='zidane', bash_command='echo passe mágico', dag=dag) 
task2 = BashOperator(task_id='Ronaldinho', bash_command='echo show', dag=dag)
task3 = BashOperator(task_id='Neymar', bash_command='echo rabisca', dag=dag) 
task4 = BashOperator(task_id='Ronaldo', bash_command='echo balanca e e gol', dag=dag)

task1 >> [task2, task3] >> task4 