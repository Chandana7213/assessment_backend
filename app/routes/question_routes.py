from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.auth_service import authenticate_user, create_access_token
from sqlalchemy.orm import Session
from app.schemas.questions import QuestionRequest


def createQuestion(db: Session, data: QuestionRequest, user_id:int):