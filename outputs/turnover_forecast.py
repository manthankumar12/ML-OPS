import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor
from snowflake.snowpark.session import Session
from snowflake.snowpark import DataFrame
from snowflake.snowpark.functions import col
from sklearn.ensemble import IsolationForest

conn_params = {
    "user": "Manthankumar",
    "password": "Ranamanthan@123",
    "account": "wyb94529",
    "warehouse": "COMPUTE_WH",
    "role": "ACCOUNTADMIN",
    "database": "SNOWLENS",
    "schema": "DEMO",
}

conn = snowflake.connector.connect(
    user=conn_params['user'],
    password=conn_params['password'],
    account=conn_params['account'],
    warehouse=conn_params['warehouse'],
    role=conn_params['role'],
    database=conn_params['database'],
    schema=conn_params['schema']
)
cur = conn.cursor()
query = "SELECT * FROM turnover"
cur.execute(query)

df = cur.fetch_pandas_all()

model = IsolationForest(contamination=0.1)  
df['label'] = model.fit_predict(df[['NET_TURNOVER']])

df['label'] = df['label'].apply(lambda x: 1 if x == -1 else 0)

cur.close()
conn.close()

print(df)
