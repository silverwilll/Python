import pandas as pd

df = pd.read_csv('exercises.csv', sep=r',', engine='python', index_col=0)

df.columns = ['Pullups', 'Pushups', 'Squats']
df.columns = df.columns.str.strip()

print(df.columns)
print(df.head())