from aiogram.types import CallbackQuery
from loader import dp, bot
from services.services import listingisTop
from utils import texts
from utils.env import ADMIN


@dp.callback_query_handler(lambda c: c.data.startswith("listing_check_"))
async def handle_check_callback(callback_query: CallbackQuery):
    listing_id = int(callback_query.data.split("_")[2])
    tg_id = int(callback_query.data.split("_")[3])
    

    is_top = listingisTop(listing_id, type="check")
    
    await bot.send_message(
        chat_id=ADMIN,
        text=texts.ADMIN_CHECK_SUCCESS
    )

    await bot.send_message(
        chat_id=tg_id,
        text=texts.USER_CHECK_SUCCESS
    )
    
