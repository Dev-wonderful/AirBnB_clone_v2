#!/usr/bin/python3
"""This module is used to connected to MySQL Using SQLAlchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize the database"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all object from database depending on cls (optional)"""
        all_objs = {}
        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City,
            'Review': Review, 'Amenity': Amenity
        }

        def get_all(cls_f):
            cls_objs = self.__session.query(classes[cls_f])
            for objs in cls_objs:
                key = f'{cls_f}.{objs.id}'
                all_objs[key] = objs
        if cls:
            if isinstance(cls, str):
                get_all(cls)
        else:
            for cls_str, cls_type in classes.items():
                get_all(cls_str)

        return all_objs

    def new(self, obj):
        """add new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.remove
