import pandas as pd

df = pd.read_excel("app/data/input/pizza.xlsx")

df["Data"] = df["Order Time"].dt.date
df["Day"] = df["Order Time"].dt.day_name()
df["Time of Order"] = df["Order Time"].dt.time
df["Time of Delivery"] = df["Delivery Time"].dt.time
