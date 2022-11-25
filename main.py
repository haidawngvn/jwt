import enum
from sqlalchemy import Integer, Enum, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TemplateStatus(enum.Enum):
    one = 1
    two = 2
    three = 3

class MyClass(Base):
    __tablename__ = 'some_table'
    id = Column(Integer, primary_key=True)
    value = Column(Enum(TemplateStatus))