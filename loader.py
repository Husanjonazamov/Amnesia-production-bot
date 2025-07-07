# loader.py fayli
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# add import
# from utils.env import BOT_TOKEN
import logging

BOT_TOKEN='7178118588:AAEAobQyB-2Uy84tfb4eK_xoeP70cAYr01I'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage) 