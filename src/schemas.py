# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import date

class LandlordCreate(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr
    Password: str
    PhoneNumber: str
    Active: bool = True

class LandlordResponse(BaseModel):
    token: str


