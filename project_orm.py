import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# User table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(64))
    gender = Column(String(50))
    group = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} | {self.name} | {self.group}"
    
# Support table
class Support(Base):
    __tablename__ = 'support'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(30))
    query = Column(String(250))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
