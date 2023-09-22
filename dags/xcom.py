from airflow import DAG
from airflow.operators.bash import BashOperator 
from airflow.operators.python import PythonOperator
from datetime import datetime 

with DAG('exemplo_xcom', description='XCOM CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) as dag:

    def task_write(**kwargs):
        kwargs['ti'].xcom_push(key='valorxcom1', value=10200) 

    def task_read(**kwargs): 
        valor = kwargs['ti'].xcom_pull(key='valorxcom1')
        print(f'valor recuperado:{valor}')
        
    task1 = PythonOperator(task_id='task1', python_callable=task_write) 
    task2 = PythonOperator(task_id='task2', python_callable=task_read)
     
task1 >> task2