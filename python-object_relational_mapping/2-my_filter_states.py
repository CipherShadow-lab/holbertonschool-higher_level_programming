#!/usr/bin/python3
"""
Script displays all values in 'states' table
of database 'hbtn_0e_0_usa' where 'name'
matches the supplied argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database to get specified state 'name'
    from database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
