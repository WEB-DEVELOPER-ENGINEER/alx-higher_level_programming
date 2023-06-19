#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_username, mysql_password, db_name),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a new session
    session = Session()

    # Create a new State object representing California
    california = State(name='California')

    # Create a new City object representing San Francisco
    san_francisco = City(name='San Francisco')

    # Add the City object to the State's cities relationship
    california.cities.append(san_francisco)

    # Add the State object to the session
    session.add(california)

    # Commit the transaction to persist the objects to the database
    session.commit()

    # Close the session
    session.close()
