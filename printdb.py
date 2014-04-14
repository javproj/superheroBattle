import sqlite3
import sys

con = sqlite3.connect('main.db')
cur = con.cursor()

with con:
    cur.execute("SELECT * FROM characters")
    rows = cur.fetchall()
    for row in rows:
        print row