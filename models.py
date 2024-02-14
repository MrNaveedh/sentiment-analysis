from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey 
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


engine = create_engine("sqlite:///mydb.db",echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Topic(Base):
    __tablename__ = "topic"

    topic_id = Column(Integer, primary_key=True)
    topic = Column(String)
    comment=relationship('Comment',backref='topic')
    

class Comment(Base):
    __tablename__ = "comment"

    comment_id = Column(Integer, primary_key=True)
    comment = Column(String)
    topic_id = Column(Integer,ForeignKey('topic.topic_id'))    
    emotions = relationship('Emotion', backref='comment')

class Emotion(Base):
    __tablename__ = "emotion"

    emotion_id = Column(Integer, primary_key=True)
    emotion_type = Column(String)
    comment_id = Column(Integer, ForeignKey('comment.comment_id'))

Base.metadata.create_all(bind=engine)