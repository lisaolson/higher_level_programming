#!/usr/bin/python3
"""Module to list all cities from hbtn_0e_4_usa
"""
import MySQLdb
import sys


db = MySQLdb.connect(
	host="localhost",
	user=sys.argv[1],
	passwd=sys.argv[2],
	db=sys.argv[3],
	port=3306
)

c = db.cursor()
c.execute("SELECT id, name FROM cities ORDER BY id ASC")
query_rows = c.fetchall()
for row in query_rows:
	print(row)
c.close()
db.close()
