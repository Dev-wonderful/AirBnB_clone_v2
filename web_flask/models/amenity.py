#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Defines what each amenity would have"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
