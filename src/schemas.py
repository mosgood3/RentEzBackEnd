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
    Id: str
    FirstName: str
    LastName: str
    Email: EmailStr
    PhoneNumber: str
    Active: bool
    ExpirationDate: date
    token: str


