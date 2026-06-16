import streamlit as st
import sqlite3
import pandas as pd

st.title("Smart Resource Monitor")

conn = sqlite3.connect("metrics.db")

df = pd.read_sql_query(
    "SELECT * FROM system_metrics",
    conn
)

st.write(df.tail(10))

st.line_chart(df["cpu_usage"])

st.line_chart(df["memory_usage"])
from sklearn.linear_model import LinearRegression

cpu_df = df[["cpu_usage"]].copy()

cpu_df["previous_cpu"] = cpu_df["cpu_usage"].shift(1)
cpu_df = cpu_df.dropna()

X = cpu_df[["previous_cpu"]]
y = cpu_df["cpu_usage"]

model = LinearRegression()
model.fit(X, y)

current_cpu = cpu_df["cpu_usage"].iloc[-1]

prediction = model.predict([[current_cpu]])

st.subheader("ML Prediction")

st.metric(
    "Predicted Next CPU Usage",
    f"{prediction[0]:.2f}%"
)