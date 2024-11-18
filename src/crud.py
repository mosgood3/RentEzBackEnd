import uuid
from datetime import datetime, date, timedelta
import requests
from config import SUPABASE_KEY, SUPABASE_URL

def create_landlord(landlord_data):
    # Generate a unique Id and the createdat timestamp
    landlord_data['Id'] = str(uuid.uuid4())  # Generate unique UUID for Id
    landlord_data['CreatedAt'] = datetime.now().isoformat()  # Current timestamp in ISO format
    landlord_data['ExpirationDate'] = (date.today() + timedelta(days=35)).strftime('%Y-%m-%d')
    landlord_data['Active'] = bool(True)
    
    # Format any date fields
    for key, value in landlord_data.items():
        if isinstance(value, date):
            landlord_data[key] = value.strftime('%Y-%m-%d')

    headers = {
        "Content-Type": "application/json",
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }

    response = requests.post(f"{SUPABASE_URL}/rest/v1/LandLords", headers=headers, json=landlord_data)

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Text: {response.text}")

    if response.status_code == 201:
        return landlord_data  # Return the modified data, including the generated Id
    else:
        raise Exception(f"Failed to create landlord: {response.status_code} {response.text}")


