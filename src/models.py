import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql import func


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
 
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique = True, nullable=False)
    date_subscription = Column(DateTime, default=func.now())

class Planet(Base):
    __tablename__ = 'planet'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(800))
    weather = Column(String(250))
    population = Column(Integer)
    
    
    

class Character(Base):
    __tablename__ = 'character'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer)
    origin_planet = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
