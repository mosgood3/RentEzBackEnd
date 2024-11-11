import requests
from app.core.config import settings

class SupabaseClient:
    def __init__(self):
        self.base_url = f"{settings.SUPABASE_URL}/rest/v1"
        self.headers = {
            "apikey": settings.SUPABASE_KEY,
            "Authorization":f"Bearer {settings.SUPABASE_KEY}",
            "Content-Type": "application/json"
        }
    def post(self,table: str, data: dict):
        url = f"{self.base_url}/{table}"
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

supabase_client = SupabaseClient()