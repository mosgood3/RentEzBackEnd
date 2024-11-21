# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import date

class LandlordCreate(BaseModel):
    Name: str
    Email: EmailStr
    Plan: str
    Password: str

class LandlordResponse(BaseModel):
    token: str


