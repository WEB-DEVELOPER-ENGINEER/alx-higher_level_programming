#!/usr/bin/python3
from relationship_state import State
from relationship_city import City, Base
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

    new_city = City(name="San Francisco")
    new_state = State(name="California")
    new_state.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
