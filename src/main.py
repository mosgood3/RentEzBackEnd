# main.py
from fastapi import FastAPI, HTTPException
from schemas import LandlordCreate, LandlordResponse
from fastapi.middleware.cors import CORSMiddleware
from crud import create_landlord
from auth import create_jwt_token

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # You can use ["*"] to allow all origins, but it's more secure to restrict this
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.post("/landlords/signup", response_model=LandlordResponse)
def signup_landlord(landlord: LandlordCreate):
    landlord_data = landlord.model_dump()  # Convert Pydantic model to dictionary

    try:
        # Create landlord in database
        created_landlord = create_landlord(landlord_data)
        
        # Generate JWT token using the manually created Id
        token = create_jwt_token(created_landlord["Id"])
        print("Generated JWT Token:", token)  # Debug: Check if token is generated
        
        # Add Id and createdat to response for consistency
        return LandlordResponse(Id=created_landlord["Id"], createdat=created_landlord["CreatedAt"], token=token)
    
    except Exception as e:
        print(f"Error during landlord signup: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")




