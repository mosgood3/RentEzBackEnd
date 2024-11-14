# main.py
from fastapi import FastAPI, HTTPException
from schemas import LandlordCreate, LandlordResponse
from crud import create_landlord
from auth import create_jwt_token

app = FastAPI()

@app.post("/landlords/signup", response_model=LandlordResponse)
def signup_landlord(landlord: LandlordCreate):
    landlord_data = landlord.model_dump()  # Convert Pydantic model to dictionary
    created_landlord = create_landlord(landlord_data)

    if not created_landlord:
        raise HTTPException(status_code=400, detail="Landlord registration failed.")

    # Generate JWT token
    token = create_jwt_token(created_landlord["Id"])
    
    return LandlordResponse(
        id=created_landlord["Id"],
        FirstName=created_landlord["FirstName"],
        LastName=created_landlord["LastName"],
        Email=created_landlord["Email"],
        PhoneNumber=created_landlord["PhoneNumber"],
        Active=created_landlord["Active"],
        ExpirationDate=created_landlord["ExpirationDate"],
        token=token
    )

