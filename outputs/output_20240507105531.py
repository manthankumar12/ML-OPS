import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col

# Define connection parameters
connection_params = {
    "ACCOUNT": "ls31517.ap-southeast-1",
    "USER": "manthan",
    "PASSWORD": "Manthanrana123",
    "ROLE": "ACCOUNTADMIN",
    "WAREHOUSE": "COMPUTE_WH",
    "DATABASE": "SNOWLENS",
    "SCHEMA": "DEMO"
}

# Create a Snowpark session using the defined connection parameters
session = Session.builder.configs(connection_params).create()

def hello(session: Session) -> DataFrame:
    df = session.table("SNOWLENS.DEMO.QUERY_HISTORY_TABLE")
    return df

# Fetch the table and display it
print(hello(session).show())
