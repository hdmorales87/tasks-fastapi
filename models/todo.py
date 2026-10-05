from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base
from db import Base


class Todo(Base):
   __tablename__ = "todos"
   id = Column(Integer, primary_key=True)
   text = Column(String)
   is_done = Column(Boolean, default=False)
