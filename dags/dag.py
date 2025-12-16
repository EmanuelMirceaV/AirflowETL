from datetime import datetime, timedelta
from airflow.sdk import DAG

#import requests
#import pandas as pd
#from bs4 import BeautifulSoup
#from airflow.operators.python import PythonOperator
#from airflow.providers.postgres import PostgresOperator
#from airflow.providers.postgres.hooks import PostgresHook

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 12, 15),
    #'email_on_failure': False,
    #'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'amazon_books_scraper',
    default_args=default_args,
    description='A DAG to scrape Amazon product data and store it in Postgres',
    schedule=timedelta(days=1), # want it to run daily
    #catchup=False,
)

'''
headers = {
    "Referer": 'https://www.amazon.com/',
    "Sec-Ch-Ua": "Not_A Brand",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "macOS",
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
'''
