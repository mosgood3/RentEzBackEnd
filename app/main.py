# app/main.py

from fastapi import FastAPI
from app.api.api_001.endpoints import landlords

app = FastAPI()

# Include the users router with a prefix and tags for organization
app.include_router(landlords.router, prefix="/v1", tags=["landlords"])

