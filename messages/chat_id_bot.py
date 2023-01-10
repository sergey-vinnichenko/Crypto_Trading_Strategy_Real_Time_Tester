import logging
from aiogram import Bot, Dispatcher, executor, types

# This file is needed in order to get the telegram chat ID number. Need to
# - Run this file
# - In the telegram chat, write the start command

# Fill in your bot token here
API_TOKEN = 'ххххх'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Hello Message
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Your chat id: " + str(message.chat.id))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
