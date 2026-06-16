import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect("metrics.db")

df = pd.read_sql_query(
    "SELECT cpu_usage FROM system_metrics",
    conn
)

df["previous_cpu"] = df["cpu_usage"].shift(1)
df = df.dropna()

X = df[["previous_cpu"]]
y = df["cpu_usage"]

model = LinearRegression()
model.fit(X, y)

current_cpu = [[df["cpu_usage"].iloc[-1]]]

prediction = model.predict(current_cpu)

print(f"Current CPU: {current_cpu[0][0]:.2f}%")
print(f"Predicted Next CPU: {prediction[0]:.2f}%")