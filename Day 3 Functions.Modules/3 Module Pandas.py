import pandas as pd

s = pd.Series([10,20,30,40])

print(s[0])
print(s[1])

data = {
    "Name": ["shivam","cr"],
    "Age": [23,14],
    "Gender": ["Male","Female"]
}

df = pd.DataFrame(data)

print(df)
print(df["Name"][1])