import pandas as pd

df = pd.read_excel("app/data/input/pizza.xlsx")

dias_ordem = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

df["Data"] = df["Order Time"].dt.date
df["Day"] = df["Order Time"].dt.day_name()
df["Day"] = pd.Categorical(df["Day"], categories=dias_ordem, ordered=True)
df["Time of Order"] = df["Order Time"].dt.time
df["Time of Delivery"] = df["Delivery Time"].dt.time
df['State'] = df['Location'].str.split(',').str[-1].str.strip()


