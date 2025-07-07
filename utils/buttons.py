# buttons.py fayli
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




def edit_check_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Qabul qilindi", callback_data="check_edit_confirm")],
        ]
    )
