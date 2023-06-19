#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conect.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    for row in cursor.fetchall():
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
    cursor.close()
    conect.close()
