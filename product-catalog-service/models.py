# model.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Products(Base):
    __tablename__ = 'products'
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    picture = Column(String)
    price_usd = Column(String)
    categories = Column(String)
