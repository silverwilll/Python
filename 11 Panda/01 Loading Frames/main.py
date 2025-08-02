import pandas as pd

df = pd.read_csv('exercises.csv', sep=r'\s*,\s*', engine='python')
print(df.columns)
print(df.head())