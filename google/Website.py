from connection import *


class Website(Base):
    __tablename__ = "Website"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    domain = Column(String)
    page_count = Column(Integer)
    HTML_ver = Column(Integer)
