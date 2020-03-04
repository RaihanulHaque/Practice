
import sqlite3

conn = sqlite3.connect('stark.db')

cursor = conn.cursor()
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for row in users :
	print(row)
conn.commit()
conn.close()