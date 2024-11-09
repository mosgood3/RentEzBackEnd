import requests

# Define your endpoint and the payload (data to send)
url = "http://127.0.0.1:8000/createLandLord"
payload = {
    "FirstName": "Alice",
    "LastName": "Smith",
    "Email": "alice@example.com",
    "Password": "password123",
    "Plan": "Premium",
    "Status": True,
    "ExpirationDate": "2025-12-31"
}

response = requests.post(url, json=payload)

# Print the raw response content
print("Response status code:", response.status_code)
print("Response text:", response.text)  # Print the raw text body of the response

try:
    # Try to parse JSON if the response is in JSON format
    print("Response JSON:", response.json())
except ValueError as e:
    print("Error parsing JSON:", e)
