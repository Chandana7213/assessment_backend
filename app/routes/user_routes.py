from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, ChangePassword
from app.services.user_service import create_user,  get_user_info, change_password, delete_user
from app.core.config import get_db
from app.core.oauth2 import get_current_user

router = APIRouter(prefix="/users", tags=['User services'])




@router.post("/create-user", response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_data.name, user_data.email, user_data.password, is_admin = user_data.is_admin)
    # return UserOut.from_orm(user)
    return user



@router.get("/user-info")
def get_user_details(db: Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    users = get_user_info(db, current_user.get('user_id'))
    return users


@router.delete('/delete-user')
def user_delete(d_user_id:int,db: Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):
    
    user = delete_user(db, d_user_id, current_user.get('user_id'))
    return user


@router.post("/change-password")
def change_user_passoword(request:ChangePassword, db: Session = Depends(get_db), current_user:UserOut= Depends(get_current_user)):

    update_password = change_password(db,current_user.get('user_id'), request.old_password, request.new_password)
    
    return update_password