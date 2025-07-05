# bot.py fayli
from aiogram import executor

from loader import dp, bot
from utils.env import ADMIN



import handlers

async def on_startup(dp):
    """
    Botni asosiy ishga tushiradigan fayl
    """
    
    await bot.send_message(
        chat_id=ADMIN,
        text="bot ishga tushdi"
    )
    

executor.start_polling(dp, on_startup=on_startup, skip_updates=True)



