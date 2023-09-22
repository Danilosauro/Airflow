from airflow import DAG 
from airflow import Dataset
from airflow.operators.python import PythonOperator
from datetime import datetime 
import pandas as pd 


dag = DAG('producer', description='PRODUCER - CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) 

mydataset = Dataset("/opt/airflow/data/Churn_new.csv") 

def my_file():  
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";") 
    dataset.to_csv("/opt/airflow/data/Churn_new.csv") 


task1 = PythonOperator(task_id='tsk1', python_callable=my_file, dag=dag, outlets=[mydataset]) 
task1