import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col

connection_params = {
    "ACCOUNT": "wyb94529",
    "USER": "Manthankumar",
    "PASSWORD": "Ranamanthan@123",
    "ROLE": "ACCOUNTADMIN",
    "WAREHOUSE": "COMPUTE_WH",
    "DATABASE": "SNOWLENS",
    "SCHEMA": "DEMO"
}

def hello(session: Session) -> DataFrame:
    df = session.table("SNOWLENS.DEMO.QUERY_HISTORY_TABLE")
    return df

if __name__ == "__main__":
    session = Session.builder.configs(connection_params).create()
    print (hello (session).show())
