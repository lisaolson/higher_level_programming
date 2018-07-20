#!/usr/bin/python3
"""Module to define class State and Base instance
"""
import MySQLdb
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
	__tablename__ = 'states'
	id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
	name = Column(String(128), nullable=False)
