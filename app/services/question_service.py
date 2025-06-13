from sqlalchemy.orm import Session
from app.models.user import User
from app.models.question import Category, Question
from fastapi import HTTPException, status, Request
from app.schemas.questions import CategoryRequest, QuestionRequest
from sqlalchemy.exc import SQLAlchemyError




def create_categories(db: Session, data:CategoryRequest, user_id: int):
    
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    category = db.query(Category).filter(Category.name == data.name).first()
    
    if category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exsits")
    
    categoryInsert = Category(name=data.name, created_by=user_id)
    
    try:
        db.add(categoryInsert)
        db.commit()
        db.refresh(categoryInsert)
        return {"details": "Category created successfully" }
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error during user creation: {str(e)}"
        )
        
def delete_categories(db: Session, category_id: int, user_id: int):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    category = db.query(Category).filter(Category.id == category_id).first()
    
    if not category:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found.") 
            
    try:
        db.delete(category)
        db.commit()
        return {"message": "Category deleted successfully."}
    except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error during user creation: {str(e)}")
        
        
def create_question(db:Session, data: QuestionRequest, user_id:int):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    question = db.query(Question).filter(Question.question == data.question).first()
    
    if question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Question already exsits")
    
    questionInsert = Question(question= data.question, answer= data.answer, marks= data.marks,created_by=user_id, category=data.category)
    
    try:
        db.add(questionInsert)
        db.commit()
        db.refresh(questionInsert)
        return {"details": "Question created successfully" }
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error during user creation: {str(e)}"
        )



def delete_question(db: Session, question_id:int, user_id:int):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    question = db.query(Question).filter(Question.id == question_id).first()
    
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found.")
    
    try:
        db.delete(question)
        db.commit()
        return {"message": "Question deleted successfully."}
    except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error during user creation: {str(e)}")
        
        
        
def getAllQuestion(db: Session, category_id:int, user_id:int):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    category = db.query(Category).filter(Category.id == category_id).first()
    
    if not category:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found.")
            
    questions = db.query(Question).filter(Question.category == category_id).all()
    
    return questions


def getAllCategory(db: Session, user_id:int):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
        
    category = db.query(Category).all()
    
    return category