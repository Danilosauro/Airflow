from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime 
import random

dag = DAG('branchs', description='BRANCHS CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) 

def randomize_number(): 
    return random.randint(1,100) 

task_random_number = PythonOperator(task_id='task_random_number',
 python_callable=randomize_number, dag=dag) 

def evalute_number(**kwargs): 
    number = kwargs['task_instance'].xcom_pull(task_ids='task_random_number')
    if number%2 ==0: 
        return 'even_task' 
    else: 
        return 'odd_task' 

branch_task = BranchPythonOperator(
    task_id= 'branch_task', 
    python_callable=evalute_number, 
    provide_context=True, 
    dag = dag
)
   
even_task = BashOperator(task_id='even_task', bash_command= 'echo "the number is even"', dag=dag)
odd_task = BashOperator(task_id='odd_task', bash_command= 'echo "the number is odd"', dag=dag)

task_random_number >> branch_task >> [even_task, odd_task]


    