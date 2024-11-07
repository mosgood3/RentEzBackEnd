import requests

url = "http://127.0.0.1:8000/landlords/"

landlord_data = {
    "name": "Matt osgood",
    "email": "johnrob@example.com",
    "phone": "123-456-7890",
    "password": "Matthew"
}
print("Landlord data being inserted:", landlord_data)

response = requests.post(url, json=landlord_data)

if response.status_code == 200:
    print("Landlord created successfully:", response.json())
else:
    print("Failed to create landlord:", response.status_code, response.text)
