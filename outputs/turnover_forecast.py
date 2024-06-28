import pandas as pd
from sklearn.ensemble import IsolationForest
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark import DataFrame

def predict_turnover(session: Session) -> DataFrame:
    # Connect to Snowflake and fetch data
    df = session.sql("SELECT * FROM turnover").to_pandas()

    # Train the Isolation Forest model
    model = IsolationForest(contamination=0.1)  
    df['label'] = model.fit_predict(df[['NET_TURNOVER']])

    # Convert labels to binary format
    df['label'] = df['label'].apply(lambda x: 1 if x == -1 else 0)

    # Create a new DataFrame with the results
    result_df = session.create_dataframe(df)
    
    return result_df
