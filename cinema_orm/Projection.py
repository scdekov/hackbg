from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from connection import *

from sqlalchemy.orm import relationship



class Projection(Base):
    __tablename__ = "Projection"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("Movie.id"))
    type = Column(String)
    date = Column(String)
    time = Column(String)
    Movie = relationship("Movie", backref="movie_id")

    def __str__(self):
        return "[{}] - {} - {}:{}".format(self.id, self.type, self.date, self.time)
