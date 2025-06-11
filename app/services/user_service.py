from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.user import User
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from app.services.auth_service import verify_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_info(db: Session, user_id:int):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    return user
    


def create_user(db: Session,name:str, email: str, password: str, **kwargs):
    
    existing_user  = db.query(User).filter(User.email == email).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists."
        )
        
    hashed_password = get_password_hash(password)
    is_admin = kwargs.get('is_admin', False)
    user = User(name=name, email=email, hashed_password=hashed_password, is_admin=is_admin)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error during user creation: {str(e)}"
        )


def delete_user(db:Session, d_user:int, user_id:int):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    delete_user = db.query(User).filter(User.id == d_user).first()
    
    if delete_user is None:
        raise HTTPException(detail=f"User not found", status_code=status.HTTP_404_NOT_FOUND)
    
    if user.is_admin:
        try:
            db.delete(delete_user)
            db.commit()
            db.refresh()
            return {'message': f'User deteleted successfully'}
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error deleting user : {str(e)}")
    else:
        raise HTTPException(detail=f'user have a lack of permission', status_code=status.HTTP_400_BAD_REQUEST)
            


def change_password(db: Session, user_id: int, old_password: str, new_password: str):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user or not verify_password(old_password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    
    hashed_new_password = get_password_hash(new_password)
    
    user.hashed_password = hashed_new_password
    
    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating password: {str(e)}"
        )
    
    return {"detail": "Password successfully updated"} 

