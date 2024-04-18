from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    usr_id = Column(Integer, autoincrement=True, index= True, primary_key=True)
    usr_phn = Column(Integer,nullable= False)

class Data(Base):
    __tablename__ = "data"
    index = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.usr_id"), index=True)
    type = Column(String)
    convo = Column(String)

class UserCreate(BaseModel):
    usr_phn: int

class DataCreate(BaseModel):
    user_id: int
    type: str
    convo: str

def create_all_tables(engine):
    Base.metadata.create_all(bind=engine)