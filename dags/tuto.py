"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.utils.dates import days_ago #set time to midnight utc


from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_arguments = {'owner':'elyse', 'start_date':days_ago(1)}

#daily: everyday at midnight,
#catchup=false so it doesn't run for each execution time in the past until now
# dag = DAG('elyse', schedule_interval='@daily', catchup=False)

with DAG(
        'elyse',
        schedule_interval='@daily',
        catchup=False,
        default_args=default_arguments
) as dags:

