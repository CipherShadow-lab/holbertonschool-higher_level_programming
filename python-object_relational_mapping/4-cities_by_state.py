#!/usr/bin/python3
"""
Script lists all 'cities' from database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database to list all 'cities' from database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)
