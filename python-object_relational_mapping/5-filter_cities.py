#!/usr/bin/python3
"""
Script takes 'state' name as an argument and lists all 'cities'
of that state using  database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database to list all 'cities' from database
    based on provided 'name' argument.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = (
        "SELECT cities.id, cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
