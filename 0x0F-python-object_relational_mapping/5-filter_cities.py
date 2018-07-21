#!/usr/bin/python3
"""Lists all cities of state given
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
    c.execute("SELECT cities.name FROM cities JOIN states\
                ON cities.state_id = states.id WHERE\
                states.name = '%s' ORDER BY cities.id ASC" % sys.argv[4])
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    db.close()
