from fastapi import FastAPI
from decouple import config
from supabase import create_client, Client

url = config("SupaBaseUrl")
key = config("SupaBaseKey")

app = FastAPI()
supabase: Client = create_client(url, key)

@app.get("/")
def test():
    return {"msg": "hello world"}