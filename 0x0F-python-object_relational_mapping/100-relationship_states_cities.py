#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    session.add_all([new, new_city])
    session.commit()
    session.close()
    session.commit()
