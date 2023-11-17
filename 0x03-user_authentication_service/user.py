#!/usr/bin/env python3
"""
    User model
"""
from typing import Optional
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

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    hashed_password: int = Column(String, nullable=False)
    session_id: Optional[str] = Column(String, nullable=True)
    reset_token: Optional[str] = Column(String, nullable=True)
