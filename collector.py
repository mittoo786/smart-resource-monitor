import psutil
import sqlite3
import time
from datetime import datetime

conn = sqlite3.connect("metrics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS system_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    cpu_usage REAL,
    memory_usage REAL
)
""")

conn.commit()

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    cursor.execute("""
    INSERT INTO system_metrics
    (timestamp, cpu_usage, memory_usage)
    VALUES (?, ?, ?)
    """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cpu, memory))

    conn.commit()

    print(f"CPU: {cpu}% | Memory: {memory}%")

    time.sleep(5)