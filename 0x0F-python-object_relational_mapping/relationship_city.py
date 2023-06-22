#!/usr/bin/python3
"""The class definition of a City"""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """City model class"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
