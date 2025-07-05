from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts


@dp.callback_query_handler(lambda call: call.data.startswith("contact_info"))
async def send_contact_info(call: CallbackQuery, state: FSMContext):
    user = call.from_user
    user_id = user.id
    
    await call.message.answer(texts.CONTACT)
    await call.answer()
