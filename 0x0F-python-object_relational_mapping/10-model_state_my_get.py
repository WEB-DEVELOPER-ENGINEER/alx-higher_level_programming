#!/usr/bin/python3
"""
Prints the State id with the name passed as argument
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and get a state
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == argv[4]).first()
    if instance is None:
        print('Not found')
    else:
        print('{}'.format(instance.id))
