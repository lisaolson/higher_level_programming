#!/usr/bin/python3
"""Module to display all values in the states table
    where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    db.close()
