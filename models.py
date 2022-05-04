from database import Base
from sqlalchemy import Column,Integer,String,Boolean

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    complete = Column(Boolean,default=False)
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String)