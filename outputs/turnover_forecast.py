import pandas as pd

from sklearn.ensemble import IsolationForest

# Fit the model
model = IsolationForest(contamination=0.1)  # Assuming 10% of data is anomalous
dataframe['label'] = model.fit_predict(dataframe[['NET_TURNOVER']])

# Convert -1 (anomaly) to 1 and 1 (normal) to 0
dataframe['label'] = dataframe['label'].apply(lambda x: 1 if x == -1 else 0)

print(dataframe)