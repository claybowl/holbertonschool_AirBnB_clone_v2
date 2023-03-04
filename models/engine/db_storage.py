#!/usr/bin/python3
'''This modules defines DBStorage class'''

from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    '''Defining class Storage'''

    __engine = None
    __session = None

    def __init__(self):
        '''Init for class DBstorage'''
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PWD, HOST, DB, ENV), pool_pre_ping=True)

        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ """
        obj_dict = {}

        if cls is not None:
            for obj in self.__session.query(cls).all():
                obj_dict.update({'{}.{}'.format(
                    type(cls).__name__, obj.id): obj})
        else:
            for class_name in all_classes.values():
                obj_list = self.__session.query(class_name)
                for obj in obj_list:
                    obj_dict.update({'{}.{}'.format(
                        type(obj).__name__, obj.id): obj})
        return obj_dict

    def new(self, obj):
        '''new obj for sql'''
        self.__session.add(obj)

    def save(self):
        '''saves through commit to db'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes an obj'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.base_model import BaseModel, Base
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        '''reloads db'''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """closes the current session"""
        self.__session.remove()
