
import snowflake.connector
import os

def create_udf():
     conn_params = {
        "user": "${{ secrets.SNOWFLAKE_USER }}",
        "password": "${{ secrets.SNOWFLAKE_PASSWORD }}",
        "account": "${{ secrets.SNOWFLAKE_ACCOUNT }}",
        "warehouse": "${{ secrets.SNOWFLAKE_WAREHOUSE }}",
        "role": "${{ secrets.SNOWFLAKE_ROLE }}",
        "database": "${{ secrets.SNOWFLAKE_DATABASE }}",
        "schema": "${{ secrets.SNOWFLAKE_SCHEMA }}"
     }
      
    # Establish connection
     connection = snowflake.connector.connect(
        user=conn_params['user'],
        password=conn_params['password'],
        account=conn_params['account'],
        warehouse=conn_params['warehouse'],
        role=conn_params['role'],
        database=conn_params['database'],
        schema=conn_params['schema']
     )

    # Read the Python function to be used in UDF
with open('outputs/turnover_forecast.py', 'r') as file:
    udf_code = file.read()

# SQL command to create the UDF
create_function_sql = f"""
CREATE OR REPLACE FUNCTION predict_turnover_udf()
RETURNS TABLE (NET_TURNOVER FLOAT, LABEL INT)
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
PACKAGES = ('snowflake-snowpark-python', 'pandas', 'scikit-learn')
HANDLER = 'turnover_forecast.predict_turnover'
AS
$$
{udf_code}
$$;
"""

    # Execute the SQL command
with connection.cursor() as cursor:
    cursor.execute(create_function_sql)
    print("Function created successfully")

# Close the connection
    connection.close()

if __name__ == "__main__":
    create_udf()



# import snowflake.connector
# import os

# def create_udf():
#     # Connection parameters
#     # conn_params = {
#     #     "user": os.getenv('SNOWFLAKE_USER'),
#     #     "password": os.getenv('SNOWFLAKE_PASSWORD'),
#     #     "account": os.getenv('SNOWFLAKE_ACCOUNT'),
#     #     "warehouse": os.getenv('SNOWFLAKE_WAREHOUSE'),
#     #     "role": os.getenv('SNOWFLAKE_ROLE'),
#     #     "database": os.getenv('SNOWFLAKE_DATABASE'),
#     #     "schema": os.getenv('SNOWFLAKE_SCHEMA')
#     # }

#      conn_params = {
#         "user": "${{ secrets.SNOWFLAKE_USER }}",
#         "password": "${{ secrets.SNOWFLAKE_PASSWORD }}",
#         "account": "${{ secrets.SNOWFLAKE_ACCOUNT }}",
#         "warehouse": "${{ secrets.SNOWFLAKE_WAREHOUSE }}",
#         "role": "${{ secrets.SNOWFLAKE_ROLE }}",
#         "database": "${{ secrets.SNOWFLAKE_DATABASE }}",
#         "schema": "${{ secrets.SNOWFLAKE_SCHEMA }}"
#     }
#     # Establish connection
# try:
#     connection = snowflake.connector.connect(
#         user=conn_params['user'],
#         password=conn_params['password'],
#         account=conn_params['account'],
#         warehouse=conn_params['warehouse'],
#         role=conn_params['role'],
#         database=conn_params['database'],
#         schema=conn_params['schema']
#     )
#     print("Connected to Snowflake successfully!")
#     # Perform further operations with Snowflake here
# except Exception as e:
#     print(f"Error connecting to Snowflake: {e}")

#     # Read the Python function to be used in UDF
#     with open('outputs/turnover_forecast.py', 'r') as file:
#         udf_code = file.read()

#     # SQL command to create the UDF
#     create_function_sql = f"""
#     CREATE OR REPLACE FUNCTION predict_turnover_udf()
#     RETURNS TABLE (NET_TURNOVER FLOAT, LABEL INT)
#     LANGUAGE PYTHON
#     RUNTIME_VERSION = '3.8'
#     PACKAGES = ('snowflake-snowpark-python', 'pandas', 'scikit-learn')
#     HANDLER = 'turnover_forecast.predict_turnover'
#     AS
#     $$
#     {udf_code}
#     $$;
#     """

#     # Execute the SQL command
#     with connection.cursor() as cursor:
#         cursor.execute(create_function_sql)
#         print("Function created successfully")

#     # Close the connection
# finally:
#     if 'connection' in locals():
#         connection.close()

# if __name__ == "__main__":
#     create_udf()
