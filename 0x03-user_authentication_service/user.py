#!/usr/bin/env python3
"""
    User model
"""
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    """
        Base
    """
    pass


class User(Base):
    """
       The base class
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(250))
    hashed_password: Mapped[str] = mapped_column(String(250))
    session_id: Mapped[Optional[str]] = mapped_column(String(250))
    reset_token: Mapped[Optional[str]] = mapped_column(String(250))
