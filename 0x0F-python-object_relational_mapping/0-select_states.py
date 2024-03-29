#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")
    for row in cur.fetchall():
        print("({}, '{}')".format(row[0], row[1]))
