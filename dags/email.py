from airflow import DAG 
from airflow.operators.bash import BashOperator 
from airflow.operators.email import EmailOperator
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

dag= DAG('email_teste', description='EMAIL DAG CURSO AIRFLOW', 
     default_args= default_args, schedule_interval=None, 
     catchup=False, default_view='graph', tags=['processo','email','tag', 'pipeline']) 

task1 = BashOperator(task_id='tsk1', bash_command='sleep 1', dag=dag) 
task2 = BashOperator(task_id='tsk2', bash_command='sleep 1', dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 1', dag=dag) 
task4 = BashOperator(task_id='tsk4', bash_command='exit 1', dag=dag)
task5 = BashOperator(task_id='tsk5', bash_command='sleep 1', trigger_rule='none_failed', dag=dag)
task6 = BashOperator(task_id='tsk6', bash_command='sleep 1', trigger_rule='none_failed', dag=dag)

send_email = EmailOperator(task_id='send_email', 
            to='danilodias_lc@hotmail.com', 
            subject='Airflow',
            html_content='''<h3>Ocorreu um erro na Dag. </h3>
                <p> Dag: send_email </p>''', 
                trigger_rule ='one_failed', dag=dag  )


[task1, task2] >> task3 >> task4 
task4 >> [task5, task6, send_email]