# app/api/api_v1/endpoints/users.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.crud.landlord import create_landlord

router = APIRouter()

class LandLordCreate(BaseModel):
    FirstName: str
    LastName: str
    PhoneNumber: str
    Email: str
    Plan: str
    Active: bool
    ExpirationDate: str  # Assuming ISO format (YYYY-MM-DD) for dates

@router.post("/landlords")
async def create_user_endpoint(user: LandLordCreate):
    """
    FastAPI endpoint to create a new user in the users table.
    """
    response = create_landlord(user.model_dump())
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response
