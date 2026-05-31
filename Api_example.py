import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()

    for user in users:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
else:
    print("Failed to fetch data")