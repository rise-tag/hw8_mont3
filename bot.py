import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from config import TOKEN
from handlers import start_bot, get_users, add_admin, remove_admin

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.message.register(start_bot, F.command("start"))
dp.message.register(get_users, F.text == "Users")
dp.callback_query.register(add_admin, F.data == 'add_admin')
dp.callback_query.register(remove_admin, F.data == 'remove_admin')

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
