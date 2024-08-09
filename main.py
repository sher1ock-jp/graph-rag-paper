import pandas as pd

# Path to your .parquet file
file_path = 'output/20240809-104350/artifacts/create_final_relationships.parquet'

# Read the .parquet file
df = pd.read_parquet(file_path)

# Display the DataFrame
print(df)