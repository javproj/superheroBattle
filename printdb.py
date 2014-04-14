import sqlite3
import sys

db = raw_input("Enter the name of the database to use: ")
con = sqlite3.connect(db)
cur = con.cursor()

with con:
    cur.execute("SELECT * FROM characters")
    rows = cur.fetchall()
    for row in rows:
        print row