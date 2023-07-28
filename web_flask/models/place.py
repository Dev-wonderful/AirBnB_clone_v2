#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from sqlalchemy.orm import relationship
from models.review import Review
import models

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """This class defines the table 'places' by various
    attributes(columns) for the database storage"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade='all, delete-orphan',
                               backref="place")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='place_amenities', viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns the reviews associated with Place"""
            reviews_in_place = []
            # getting a list of values from the all() dictionary and looping
            for value in models.storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_in_place.append(value)
            return reviews_in_place

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place"""
            from models.amenity import Amenity
            amenities_in_place = []
            # getting a list of values from the all() dictionary and looping
            # through to check if the id is in amenity_ids
            for value in models.storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_in_place.append(value)
            return amenities_in_place

        @amenities.setter
        def amenities(self, amenity_id):
            """Setter that handles append method for adding an Amenity.id
            to the attribute amenity_ids"""
            from models.amenity import Amenity
            if type(amenity_id) == Amenity:
                self.amenity_ids.append(amenity_id)
