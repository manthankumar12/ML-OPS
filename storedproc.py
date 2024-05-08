# storedproc.py file
import snowflake.connector
from snowflake.snowpark.session import Session 

def run(message):    
  return "hello world, v1";

connection_params = {
    "ACCOUNT": "ls31517.ap-southeast-1",
    "USER": "manthan",
    "PASSWORD": "Manthanrana123",
    "ROLE": "ACCOUNTADMIN",
    "WAREHOUSE": "COMPUTE_WH",
    "DATABASE": "SNOWLENS",
    "SCHEMA": "DEMO"
}

if __name__ == "__main__":
    session = Session.builder.configs(connection_params).create()
    print (hello (session).show())
