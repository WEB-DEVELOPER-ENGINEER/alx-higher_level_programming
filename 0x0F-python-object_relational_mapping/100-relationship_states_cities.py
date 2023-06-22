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

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    session.close()
