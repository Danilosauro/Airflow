from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime 
import pandas as pd 


dag = DAG('pythonoperator', description='PYTHON OPERATOR CURSO AIRFLOW', 
     schedule_interval=None, start_date=datetime(2023,3,5), 
     catchup=False) 


def cleaning_data(): 
    dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep =";")

    dataset.columns = ["ID", "Score", "Estado", "Genero", "Idade", "Patrimonio", 
    "Saldo", "Produtos","TemCartCredito", "Ativo","Salario","Saiu"]

    
    dataset['Salario'] = dataset['Salario'].fillna(dataset['Salario'].median()) 
    dataset['Genero'] = dataset['Genero'].fillna(dataset['Genero'].mode())
    dataset['Idade'] = dataset['Idade'].fillna(dataset['Idade'].mode()) 

    dataset.to_csv('/opt/airflow/data/Churn_Clean.csv', sep=';', index=False) 
 

task1 = PythonOperator(task_id='tsk1', python_callable=cleaning_data, dag=dag) 

task1