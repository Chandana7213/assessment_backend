from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import authenticate_user, create_access_token
from app.core.config import SessionLocal, get_db
from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=['Auth services'])


# @router.post("/login", response_model=TokenResponse)
# def login(request: LoginRequest, db: Session = Depends(get_db)):
#     user = authenticate_user(db, request.email, request.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     access_token_expires = timedelta(minutes=30)
#     token = create_access_token(data={"sub": user.email, "id": user.id}, expires_delta=access_token_expires)
#     return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=TokenResponse)
# def login(request: LoginRequest, db: Session = Depends(get_db)):
def login(request: OAuth2PasswordRequestForm= Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=30)
    token = create_access_token(data={"sub": user.email, "id": user.id }, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer", "user_name":user.name, "is_admin":user.is_admin, "name":"naveen"}
