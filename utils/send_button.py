import requests
from utils.env import WEBAPP_URL, BOT_TOKEN
from utils import texts


def send_webapp_button(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "👋 Assalomu alaykum! Quyidagi tugmalar orqali kerakli bo‘limni tanlang:",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "🛒 Magazin",
                        "web_app": {
                            "url": f"{WEBAPP_URL}"
                        }
                    },
                    {
                        "text": "📞 Bog‘lanish uchun",
                        "callback_data": "contact_info"
                    }

                ]
            ]
        }
    }
    response = requests.post(url, json=payload)

    if not response.ok:
        print("❌ Inline tugma yuborishda xatolik:", response.text)



def set_menu_webapp():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setChatMenuButton"
    payload = {
        "menu_button": {
            "type": "web_app",
            "text": "📢 E'lonlar",
            "web_app": {
                "url": f"{WEBAPP_URL}"
            }
        }
    }
    response = requests.post(url, json=payload)

    if not response.ok:
        print("❌ Menu tugmasi qo'shishda xatolik:", response.text)
