from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String


Base = declarative_base()
engine = create_engine("sqlite:///data.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
