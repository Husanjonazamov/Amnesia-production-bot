from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts
from utils.env import ADMIN


@dp.message_handler(content_types=["text", "photo", "video", "sticker", "voice", "document", "audio"], state="*")  
async def default_handler(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN:
        if message.text not in ["/start", "/help"]:
            await message.answer(texts.DEFAULT_TEXT)
        elif not message.text:
            await message.answer(texts.DEFAULT_TEXT)
