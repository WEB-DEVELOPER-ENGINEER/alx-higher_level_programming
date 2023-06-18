#!/usr/bin/python3
import sys
import MySQLdb


"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""


def list_states(username, password, db_name):
    '''
        List all the states in the given db
    '''
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, passwd, db_name)
