from airflow import DAG
from airflow.operators.python import PythonOperator 
from airflow.models.variable import Variable
from datetime import datetime 


dag = DAG('variaveis', description='VARIAVEIS CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False)

def print_variable(**kwargs): 
    minhavar = Variable.get('minha_var') 
    print(f'O valor da variável é: {minhavar}')
   
        
task1 = PythonOperator(task_id='task1', python_callable=print_variable, dag=dag) 

task1
    