from airflow import DAG
from airflow.utils.email import send_email 
from airflow.operators.python import PythonOperator 
from datetime import datetime, timedelta  


default_args = { 
    'dependes_on_past' : False, 
    'start_date': datetime(2023,3,5),
    'email': ['danilodias_lc@hotmail.com'], 
    'email_on_failure': True, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(seconds=10)
}

with DAG('email_teste', description='EMAIL DAG CURSO AIRFLOW', 
     default_args= default_args, schedule_interval=None, 
     catchup=False, default_view='graph', tags=['processo','email','tag', 'pipeline']): 

    def envia_email(email):
        send_email(email, subject='Airflow', html_content='<h3ocorreu um erro</h3>>') 

    task1 = PythonOperator(task_id='tsk1', python_callable=envia_email('danilodias_lc@hotmail.com')) 

task1