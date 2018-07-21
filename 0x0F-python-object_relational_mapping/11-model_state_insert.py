#!/usr/bin/python3
"""Adds State object to the database
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
    state_lou = State(name="Louisiana")

    session.add(state_lou)
    session.commit()

    print(state_lou.id)
    session.close()
