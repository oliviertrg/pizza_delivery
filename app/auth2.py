from jose import JWSError,jwt
from app import schema
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime,timedelta
from app.config import get_authen

SECRET_KEY = get_authen()["SECRET_KEY"]
ALGORITHM = get_authen()["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = get_authen()["ACCESS_TOKEN_EXPIRE_MINUTES"]

oath2_schema = OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data: dict) :
    to_token = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_token.update({"exp" : expire})
    encode_jwt = jwt.encode(to_token,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token : str , credentials_exception) :
    try :
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        user_id : str = payload.get("user_id")
        if user_id is None :
            raise credentials_exception
        token_data = schema.tokendata(id = user_id)
    except JWSError :
        raise credentials_exception
    return token_data

def get_current_user(token : str = Depends(oath2_schema)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"COULD NOT VALIDATE CREDENTIALS",
                                          headers={"WWW-Authenticate": "Bearer"})
    return verify_access_token(token ,credentials_exception)
