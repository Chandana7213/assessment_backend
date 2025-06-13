from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.questions import QuestionRequest, CategoryRequest
from app.schemas.user import UserOut
from app.services.question_service import create_question, delete_question, create_categories, delete_categories, getAllCategory, \
    getAllQuestion
from app.core.config import get_db
from app.core.oauth2 import get_current_user



router = APIRouter(prefix="/api", tags=['Question services'])


@router.post("/quest-create")
def createQuestion(data: QuestionRequest, db: Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    return create_question(db, data,current_user.get('user_id'))

@router.get("/list-question/{category_id}/")
def listQuestions(category_id:int, db: Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    return getAllQuestion(db, category_id, current_user.get('user_id') )

@router.delete("/quest-delete")
def deleteQuestion(question_id:int, db:Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    return delete_question(db,question_id,current_user.get('user_id'))

@router.post("/category-create")
def createQuestion(data: CategoryRequest, db: Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    return create_categories(db, data,current_user.get('user_id'))

@router.get("/list-category")
def listCategory( db: Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    return getAllCategory(db, current_user.get('user_id') )

@router.delete("/category-delete")
def deleteCategory(category_id:int, db:Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    return delete_categories(db,category_id,current_user.get('user_id'))