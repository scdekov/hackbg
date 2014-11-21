from sqlalchemy import Column, Integer, String, Float
from connection import *


class Movie(Base):
    __tablename__ = "Movie"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def __str__(self):
        return "[{}] - {} - {}".format(self.id, self.name, self.rating)

