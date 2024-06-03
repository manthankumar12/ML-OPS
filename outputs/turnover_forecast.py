import snowflake.connector
import pandas as pd
from sklearn.ensemble import IsolationForest
from datetime import datetime
import sys

def create_snowflake_table(conn):
    try:
        cur = conn.cursor()

        # Define Snowflake SQL statements to create table
        create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS model_results (
                date TIMESTAMP_NTZ,
                net_turnover NUMBER,
                label BOOLEAN
            )
        """

        # Execute SQL statements
        cur.execute(create_table_sql)

        # Commit the transaction
        conn.commit()

        # Close cursor
        cur.close()

        print("Table created successfully.")
    except Exception as e:
        print(f"Error occurred while creating Snowflake table: {str(e)}")

def insert_results_into_snowflake(conn, df):
    try:
        cur = conn.cursor()

        # Insert data into the Snowflake table
        for index, row in df.iterrows():
            insert_sql = f"""
                INSERT INTO model_results (date, net_turnover, label) VALUES (%s, %s, %s)
            """
            cur.execute(insert_sql, (row["date"], row["net_turnover"], row["label"]))

        # Commit the transaction
        conn.commit()

        # Close cursor
        cur.close()

        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error occurred while inserting data into Snowflake table: {str(e)}")

def main():
    conn_params = {
        "user": "Manthankumar",
        "password": "Ranamanthan@123",
        "account": "wyb94529",
        "warehouse": "COMPUTE_WH",
        "role": "ACCOUNTADMIN",
        "database": "SNOWLENS",
        "schema": "demo",
    }

    # Connect to Snowflake and execute the query
    try:
        conn = snowflake.connector.connect(
            user=conn_params["user"],
            password=conn_params["password"],
            account=conn_params["account"],
            warehouse=conn_params["warehouse"],
            role=conn_params["role"],
            database=conn_params["database"],
            schema=conn_params["schema"],
        )
        cur = conn.cursor()
        query = "SELECT * FROM turnover"
        cur.execute(query)

        df = cur.fetch_pandas_all()

        # Add a 'date' column with the current timestamp
        df["date"] = datetime.now()

        # Specify the column used for model fitting
        feature_column = "NET_TURNOVER"
        model = IsolationForest(contamination=0.1)
        model.fit(df[[feature_column]])

        df["label"] = model.predict(df[[feature_column]])

        df["label"] = df["label"].apply(lambda x: 1 if x == -1 else 0)

        cur.close()

        print(df)

        # Call the function to create the Snowflake table
        create_snowflake_table(conn)

        # Call the function to insert results into the Snowflake table
        insert_results_into_snowflake(conn, df)

        # Close the connection
        conn.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
