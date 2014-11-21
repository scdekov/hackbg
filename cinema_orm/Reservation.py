from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import *


class Reservation(Base):
    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("Projection.id"))
    row = Column(Integer)
    col = Column(Integer)
    Projection = relationship("Projection", backref="projection_id")

    def __str__(self):
        return "[{}] - {} - row:{}, col:{}".format(self.id, self.username, self.row, self.col)
