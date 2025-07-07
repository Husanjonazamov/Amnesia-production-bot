from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts
from services.services import listingisTop
from utils.env import ADMIN



@dp.callback_query_handler(lambda call: call.data.startswith("listing_cancel_"), state="*")
async def cancel_query(callback: CallbackQuery, state: FSMContext):
    listing_id = int(callback.data.split("_")[2])
    tg_id = int(callback.data.split("_")[3])
    
    
    is_top = listingisTop(listing_id, type="cencel")
    
    await callback.message.answer(
        text=texts.CANCEL_LISTING
    )
    await bot.send_message(
        chat_id=ADMIN,
        text=texts.CANCEL_LISTING_ADMIN.format(listing_id)
    )