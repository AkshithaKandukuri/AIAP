import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the dataset
df = pd.read_csv('iot_sensor.csv')

# Handle Missing Values (forward fill)
df.ffill(inplace=True)

# Remove Sensor Drift (rolling mean)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)
df['temperature'] = df['temperature'].rolling(window=3).mean()
df['humidity'] = df['humidity'].rolling(window=3).mean()

# Normalize Readings (standard scaling)
scaler = StandardScaler()
df[['temperature', 'humidity']] = scaler.fit_transform(df[['temperature', 'humidity']])

# Encode Categorical Sensor IDs (one-hot encoding)
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
sensor_encoded = encoder.fit_transform(df[['sensor_id']])
sensor_df = pd.DataFrame(sensor_encoded, columns=encoder.get_feature_names_out(['sensor_id']), index=df.index)
df = pd.concat([df.drop('sensor_id', axis=1), sensor_df], axis=1)

# Display the head and info of the processed data
print("Processed Data Head:")
display(df.head())

print("\nProcessed Data Info:")
df.info()