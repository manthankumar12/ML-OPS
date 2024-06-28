import snowflake.connector

def create_udf():
    # Connection parameters
    conn_params = {
        "user": ${{ secrets.SNOWFLAKE_USER }},
        "password": ${{ secrets.SNOWFLAKE_PASSWORD }},
        "account": ${{ secrets.SNOWFLAKE_ACCOUNT }},
        "warehouse": ${{ secrets.SNOWFLAKE_WAREHOUSE }},
        "role": ${{ secrets.SNOWFLAKE_ROLE }},
        "database": ${{ secrets.SNOWFLAKE_DATABASE }},
        "schema": ${{ secrets.SNOWFLAKE_SCHEMA }},
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
