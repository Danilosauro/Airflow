from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime 

with DAG('quarta_dag', description='DAG 4 CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) as dag:

     task1 = BashOperator(task_id='task1', bash_command='sleep 5') 
     task2 = BashOperator(task_id='task2', bash_command='sleep 5')
     task3 = BashOperator(task_id='task3', bash_command='sleep 5') 
     task4 = BashOperator(task_id='task4', bash_command='sleep 5')

     ## exemplo de ordenação das tasks com python 
     ## set_upstream sequencia em ordem descrescente
     task1.set_upstream(task2)
     task2.set_upstream(task3) 
     task3.set_upstream(task4)