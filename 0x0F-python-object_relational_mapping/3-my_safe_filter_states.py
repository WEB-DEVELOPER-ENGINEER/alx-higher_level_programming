#!/usr/bin/python3
"""
Displays all values in the states
where `name` matches the argument.
Safe from SQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the states
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT * FROM states WHERE name LIKE BINARY %(name)s
            ORDER BY states.id ASC """, {'name': argv[4]})
        rows = cur.fetchall()
    if rows is not None:
        for row in rows:
            print("({}, '{}')".format(row[0], row[1]))
