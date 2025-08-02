import pandas as pd
import numpy as np

data = {
    "Mon": [1, 2, 3],
    "Tue": [0.1, 0.2, 0.3],
    "Wed": [5, 6, 7],
}

df = pd.DataFrame(data, index =["Coffee", "Tea", "Water"])
print(df)

df *= .3
print()
print(df)

df = np.sin(df)
print()
print(df)

df.loc["Coffee": "Tea"] -= 100
print()
print(df)

df.iloc[0:1] *= 2
print()
print(df)