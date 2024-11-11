# app/crud/user.py

from app.core.security import supabase_client

def create_landlord(data: dict):
    """
    Function to create a user in the 'users' table in Supabase.
    """
    try:
        response = supabase_client.post("LandLords", data)
        return response  # Response from Supabase (likely a JSON object)
    except Exception as e:
        # Handle the error gracefully
        return {"error": str(e)}
