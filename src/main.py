from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import requests
from config import SUPABASE_KEY, SUPABASE_URL

app = FastAPI()

class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    name: str

@app.post("/signup")
async def signup_user(data: UserSignUp):
    # Headers for Supabase authentication
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }

    # Payload for creating a user in auth.users
    auth_payload = {
        "email": data.email,
        "password": data.password,
        "Display name": data.name
    }

    # Create user in auth.users
    response = requests.post(f"{SUPABASE_URL}/auth/v1/signup", json=auth_payload, headers=headers)

    if response.status_code != 200:
        # Return error message if the request fails
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return {"message": "User created successfully. Please confirm your email."}



