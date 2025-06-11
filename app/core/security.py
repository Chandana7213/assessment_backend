from datetime import datetime, timedelta
from jose import jwt, JWTError
import os
from app.schemas.config import settings

# SECRET_KEY = os.getenv("SECRET_KEY", "myverysecretkey123")
# ALGORITHM = "HS256"

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str, credentials_exception):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None:
            raise credentials_exception
        return {'username':username, 'user_id': user_id}
    
    except JWTError:
        raise credentials_exception