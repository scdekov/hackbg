from connection import *


class Page(Base):
    __tablename__ = "Page"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    #title = Column(String)
    # website_id = Column(String, ForeignKey("Website.id"))
    # desc = Column(String)
    # ads = Column(Integer)
    # SSL = Column(Integer)
    # points = Column(Integer)
    # multy_lang = Column(Integer)
    # Website = relationship("Website", backref="website_id")
