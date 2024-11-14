# auth.py
import jwt
from datetime import datetime, timedelta
from config import JWT_SECRET, JWT_ALGORITHM

def create_jwt_token(landlord_id: str):
    expiration = datetime.now() + timedelta(days=35)  # Set token expiration time
    payload = {"sub": landlord_id, "exp": expiration}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
