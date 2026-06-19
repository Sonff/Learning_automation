# =====================================================================
# TASK MANAGER PROJECT: JWT AUTH & SECURITY (auth.py)
# =====================================================================
# Users verification, password hashing, and OAuth2/JWT token parsing.

from datetime import datetime, timedelta, timezone
from typing import Dict, Any
import jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .database import db

# Configuration
JWT_SECRET = "super-secret-agentic-hash-key-9999" # In production, load this from .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing utilities
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# ---------------------------------------------------------------------
# JWT Token Generator
# ---------------------------------------------------------------------
def create_access_token(data: Dict[str, Any]) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


# ---------------------------------------------------------------------
# Dependency: Extract & Authenticate Token (get_current_user)
# ---------------------------------------------------------------------
# OAuth2PasswordBearer auto-reads "Authorization: Bearer <token>" from headers
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> Dict[str, Any]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials / Token expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the JWT token
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
        
    # Check if user exists in database
    user = db.get_user(username)
    if user is None:
        raise credentials_exception
        
    return user # Returns validated user info to endpoint
