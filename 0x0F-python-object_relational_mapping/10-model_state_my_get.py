#!/usr/bin/python3
"""Prints State object with name passed in
"""

import MySQLdb
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).filter(State.name.contains(sys.argv[4])).order_by(State.id).all():
        if state is None:
            print("Not found")
        else:
            print("{}".format(state.id))

    session.close()
