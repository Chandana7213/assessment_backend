from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import Base



class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    Created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    
    cate_quest = relationship('Question', foreign_keys= "Question.category", back_populates='quest_cate')
    
    
class Question(Base):
    
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(255), index=True, nullable=False)
    answer = Column(String(255), index=True, nullable=False)
    marks = Column(Integer, nullable=True)
    category = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    Created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    
    user = relationship('User', foreign_keys=[created_by], back_populates='question')
    quest_cate = relationship('Category', foreign_keys=[category], back_populates='cate_quest')