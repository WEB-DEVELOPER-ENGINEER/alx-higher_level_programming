#!/usr/bin/python3
"""
Adds a new State  to the database `hbtn_0e_6_usa`
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """
    Access the database and add a state
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True)
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    lou_state = State(name='Louisiana')
    session.add(lou_state)
    session.commit()
    session.close()
    print('{}'.format(lou_state.id))
