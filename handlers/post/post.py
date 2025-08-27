from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import userList
from loader import dp, bot
from utils.env import ADMIN


@dp.message_handler(content_types=['text', 'photo', 'video'], state="*")
async def post(message: Message, state: FSMContext):
    
    if message.from_user.id == ADMIN:
        users = userList()
        print(users)
        success = 0  # nechta foydalanuvchiga yuborilganini hisoblaymiz

        for user in users:
            user_id = user.get('user_id')
            print(user_id)
            if not user_id:
                continue

            try:
                if message.text:
                    await bot.send_message(chat_id=user_id, text=message.text)

                elif message.photo:
                    photo_id = message.photo[-1].file_id
                    caption = message.caption if message.caption else ""
                    await bot.send_photo(chat_id=user_id, photo=photo_id, caption=caption)

                elif message.video:
                    video_id = message.video.file_id
                    caption = message.caption if message.caption else ""
                    await bot.send_video(chat_id=user_id, video=video_id, caption=caption)

                success += 1 

            except Exception as e:
                print(f"Xatolik foydalanuvchi {user_id} ga yuborishda: {e}")

        await message.answer(f"✅ Сообщение успешно отправлено {success} пользователям.")
   
        
