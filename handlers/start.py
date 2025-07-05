# start.py fayli
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import send_button




@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    chat_id = message.chat.id
    send_button.send_webapp_button(chat_id)
    
    send_button.set_menu_webapp()