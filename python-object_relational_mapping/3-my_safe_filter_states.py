#!/usr/bin/python3
"""
Script displays all values in 'states' table
of database 'hbtn_0e_0_usa' where 'name'
matches the supplied argument. 
This time safe from SQL injections!
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)
