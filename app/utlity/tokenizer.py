from itsdangerous import URLSafeTimedSerializer
from passlib.context import CryptContext
from fastapi import HTTPException

# Configuration
SECRET_KEY = "YHGBJEUGYBHJEKDUSBJUJSDWRFW"
SECURITY_PASSWORD_SALT = "HVBGH_EJYSHDBJSVBHJSDVYUHVQWIAGUQBIAGBQUH"

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Token serializer
serializer = URLSafeTimedSerializer(SECRET_KEY)

def generate_reset_token(email: str):
    return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)

def verify_reset_token(token: str, expiration: int = 18000):  # 5 hours = 18000 seconds
    try:
        email = serializer.loads(token, salt=SECURITY_PASSWORD_SALT, max_age=expiration)
        return email
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
