import requests

url = "https://reqres.in/api/users?page=1"

response = requests.get(url)

assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

print("Request was successful! Status Code: 200")

data = response.json()
users = data.get('data', [])
for user in users:
    print(f"ID: {user['id']}")
    print(f"Name: {user['first_name']} {user['last_name']}")
    print(f"Email: {user['email']}")
    print(f"Avatar: {user['avatar']}")
    print("-" * 40)
