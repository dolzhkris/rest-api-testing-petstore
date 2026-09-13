import requests
import json
import time

BASE_URL = "https://petstore.swagger.io/v2"
USERNAME = "KRIS_TEST"

def create_user():
    user_data = {
        "id": 1001,
        "username": USERNAME,
        "firstName": "Kris",
        "lastName": "Dolzh",
        "email": "kris@example.com",
        "password": "12345",
        "phone": "88005553535",
        "userStatus": 1
    }
    response = requests.post(f"{BASE_URL}/user", json=user_data)
    print("Create User:", response.json())

def get_user():
    response = requests.get(f"{BASE_URL}/user/{USERNAME}")
    print("Get User:", response.json())

def update_user():
    updated_data = {
        "id": 1001,
        "username": USERNAME,
        "firstName": "KrisUpdated",
        "lastName": "DolzhUpdated",
        "email": "kris_updated@example.com",
        "password": "54321",
        "phone": "89006663636",
        "userStatus": 1
    }
    response = requests.put(f"{BASE_URL}/user/{USERNAME}", json=updated_data)
    print("Update User:", response.json())

def delete_user():
    response = requests.delete(f"{BASE_URL}/user/{USERNAME}")
    print("Delete User:", response.json())

if __name__ == "__main__":
    create_user()
    time.sleep(0.5)
    get_user()
    time.sleep(0.5)
    update_user()
    time.sleep(0.5)
    get_user()
    time.sleep(0.5)
    delete_user()
