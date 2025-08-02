import pandas as pd

df = pd.read_csv('exercises.csv', sep=r',', index_col=0)
df.columns = df.columns.str.strip()


print(df.at['Tue', 'Pushups'])
df.at['Tue', 'Pushups'] = 50

print("Monday squats", df.iat[0, 2])

print(df)