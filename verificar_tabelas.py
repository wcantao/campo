import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("PRAGMA table_info(relatorios)")
print(c.fetchall())

conn.close()
