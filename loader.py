# loader.py fayli
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# add import
# from utils.env import BOT_TOKEN
import logging

BOT_TOKEN='7178118588:AAHE5WeED99ybl7ewW5FU7mu8kM6ySTeka8'




logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage) 