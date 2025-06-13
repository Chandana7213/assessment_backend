from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.core.config import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    Created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    Updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    question = relationship('Question', foreign_keys='Question.created_by', back_populates='user')



# class Project(Base):
    
#     __tablename__ = "projects"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50), index=True, nullable=False)
#     Created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
#     Updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)