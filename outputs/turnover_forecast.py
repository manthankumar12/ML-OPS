import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor
from snowflake.snowpark.session import Session
from snowflake.snowpark import DataFrame
from snowflake.snowpark.functions import col
from sklearn.ensemble import IsolationForest

connection_params = {
    "ACCOUNT": SF_ACCOUNT,
    "USER": SF_USER,
    "PASSWORD": SF_PASSWORD,
    "ROLE": SF_ROLE,
    "WAREHOUSE": SF_WAREHOUSE,
    "DATABASE": SF_DATABASE,
    "SCHEMA": SF_SCHEMA,
}


def hello(session: Session) -> DataFrame:
    df = session.table("SNOWLENS.DEMO.TURNOVER")
    return df


if __name__ == "__main__":
    session = Session.builder.configs(connection_params).create()
    print(hello(session).show())