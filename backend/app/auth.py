from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users = {
    "admin": "$2b$12$1S7sCldgbDcnZV1sf4DhT.byaCbIN6MkXETwqos5W/NaVn824IWVa"
}

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict, expires_minutes=60):
    payload = {
        "sub": data["sub"],
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(username, password):
    if username not in fake_users:
        return False
    return verify_password(password, fake_users[username])