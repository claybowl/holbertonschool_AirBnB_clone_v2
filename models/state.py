#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', backref='state', cascade="all, delete, delete-orphan")

    else:
        @property
        def cities(self):
            from models import storage, city
            dics = storage.all(city.City)
            diclist = []
            for v in dics.values():
                if v.state_id == self.id:
                    diclist.append(v)
            return diclist
