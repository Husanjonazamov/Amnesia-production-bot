# services.py fayli
import requests
from utils.env import BASE_URL


def userList():
    url = f"{BASE_URL}/users-list/"
    response = requests.get(url)
    
    try:
        data = response.json()
        return data
    except: 
        return []
