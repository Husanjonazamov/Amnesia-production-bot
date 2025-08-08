import requests
from utils.env import WEBAPP_URL, BOT_TOKEN
from utils import texts


def send_webapp_button(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "👋 Здравствуйте! Пожалуйста, выберите нужный раздел с помощью кнопок ниже:",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "🛒 Магазин",
                        "web_app": {
                            "url": f"{WEBAPP_URL}"
                        }
                    },
                    {
                        "text": "📞 Связаться с нами",
                        "callback_data": "contact_info"
                    }
                ]
            ]
        }
    }
    response = requests.post(url, json=payload)
    

    if not response.ok:
        print("❌ Ошибка при отправке инлайн-кнопки:", response.text)


def set_menu_webapp():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setChatMenuButton"
    payload = {
        "menu_button": {
            "type": "web_app",
            "text": "📢 Объявления",
            "web_app": {
                "url": f"{WEBAPP_URL}"
            }
        }
    }
    response = requests.post(url, json=payload)

    if not response.ok:
        print("❌ Ошибка при добавлении кнопки меню:", response.text)
