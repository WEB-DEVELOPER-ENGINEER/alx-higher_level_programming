#!/usr/bin/python3
"""
lists all cities from the database
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conect.cursor()
    cursor.execute("""SELECT cities.name
    FROM cities JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %(name)s
    ORDER BY cities.id ASC""", {'name': argv[4]})
    print(", ".join([x[0] for x in cur.fetchall()]))
    cursor.close()
    conect.close()
