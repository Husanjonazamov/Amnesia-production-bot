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


def CartNotification():
    url = f"{BASE_URL}/notification/"
    
    try:
        response = requests.get(url)
        print("Response:", response.text)
        print("Status code:", response.status_code)    

        data = response.json()

        # Faqat notifications ro'yxatini qaytarish
        return data.get("notifications", [])
        
    except Exception as e:
        print(f"CartNotification xatolik: {e}")
        return []