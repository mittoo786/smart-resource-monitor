import sqlite3

conn = sqlite3.connect("metrics.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM system_metrics")

rows = cursor.fetchall()

for row in rows:
    print(row)