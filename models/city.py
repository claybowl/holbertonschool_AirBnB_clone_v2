#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    """ class City, containing state ID, place, and name """

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
