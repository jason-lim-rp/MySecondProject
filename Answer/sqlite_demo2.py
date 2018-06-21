import sqlite3

conn = sqlite3.connect("C:\\CET\\demo.sqlite")
cur = conn.cursor()
cur.execute("SELECT * FROM Employees LIMIT 3")
rows = cur.fetchall()
for row in rows:
    print (row)
conn.close()

