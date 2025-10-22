#!/usr/bin/python3
""" Script lists all states with a name starting with N """

import MySQLdb
from sys import argv

conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
)

cur = conn.cursor()
cur.execute(SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC)
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()
