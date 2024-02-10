from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///mydb.db",echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    feedBack = Column(String)
    

Base.metadata.create_all(bind=engine)