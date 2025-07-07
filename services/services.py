# services.py fayli
import requests
from utils.env import BASE_URL



def listingisTop(listing_id, type):
    print(listing_id)
    url = f"{BASE_URL}/listing/top/{type}/{listing_id}/"
    response = requests.post(url)
    
    print(response.status_code)
    
    try:
        data = response.json()
        return data
    except Exception as e:
        return e