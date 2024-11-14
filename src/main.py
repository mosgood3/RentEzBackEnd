# main.py
from fastapi import FastAPI, HTTPException
from schemas import LandlordCreate, TokenResponse
from crud import create_landlord
from auth import create_jwt_token

app = FastAPI()

@app.post("/landlords/signup", response_model=TokenResponse)
def signup_landlord(landlord: LandlordCreate):
    landlord_data = landlord.model_dump()  # Convert Pydantic model to dictionary

    try:
        # Create landlord in database
        created_landlord = create_landlord(landlord_data)
        
        if not created_landlord:
            raise HTTPException(status_code=400, detail="Landlord registration failed.")
        
        # Generate JWT token
        token = create_jwt_token(created_landlord["Id"])
        
        # Return token only
        return TokenResponse(token=token)
    
    except Exception as e:
        print(f"Error during landlord signup: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


