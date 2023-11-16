#!/usr/bin/env python3
"""
    User model
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
       The base class
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=True)
    hashed_password = Column(String, nullable=True)
    session_id = Column(String, nullable=False)
    reset_token = Column(String, nullable=False)
