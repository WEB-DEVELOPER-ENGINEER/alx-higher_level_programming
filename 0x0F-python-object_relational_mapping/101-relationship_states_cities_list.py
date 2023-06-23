#!/usr/bin/python3
"""Database hbtn_0e_100_usa"""
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys
"""
    Module
"""


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                            sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3])

    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()
    for row in query:
        print("{}: {}".format(row.id, row.name))
        for city_row in row.cities:
            print("\t{}: {}".format(city_row.id, city_row.name))
    session.close()
