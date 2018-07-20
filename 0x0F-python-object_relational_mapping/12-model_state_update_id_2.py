#!/usr/bin/python3
"""Module to list all State objects from the database hbtn_0e_6_usa
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

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

changed_state = session.query(State).filter_by(id=2).first()

changed_state.name = "New Mexico"

session.add(changed_state)

session.commit()

session.close()
