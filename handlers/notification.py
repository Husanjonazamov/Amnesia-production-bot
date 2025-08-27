import asyncio
from services.services import CartNotification
from loader import dp, bot
from aiogram import types


tasks = {}

async def send_cart_updates():
    while True:
        try:
            notifications = CartNotification() 
            for notification in notifications:
                tg_id = notification.get("tg_id")
                items = notification.get("products", [])

                if tg_id and items:
                    product_lines = "\n".join([f"• {item['book']}" for item in items])

                    message_text = (
                        f"🛒 Ваши товары ждут вас в корзине!\n\n"
                        f"{product_lines}\n\n"
                        "Не упустите возможность оформить заказ! 😉"
                    )

                    await bot.send_message(tg_id, message_text)

        except Exception as e:
            print(f"Xatolik: {e}")

        await asyncio.sleep(86400)
