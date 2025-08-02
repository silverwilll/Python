import pandas as pd

df = pd.read_csv('exercises.csv', sep=r',', index_col=0)
df.columns = df.columns.str.strip()

print(df)

print(df.loc["Mon":"Sun":2])
print(df.loc[["Fri", "Mon"], "Puashup":"Squats"])
print(df.loc[:, "Puashup":"Squats"])

print(df.iloc[:, 1:3])