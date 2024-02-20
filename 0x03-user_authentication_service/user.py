#!/usr/bin/env python3
"""
module that creates a module user from the declarative class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    class that implements a User model

    Attributes:
           id (int): The primary key of the user.
           email (str): The email address of the user (non-nullable).
           hashed_password (str): The hashed password of the user
           (non-nullable).
           session_id (str, optional): The session ID of the user
           (nullable).
           reset_token (str, optional): The reset token of the user
           (nullable).
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
