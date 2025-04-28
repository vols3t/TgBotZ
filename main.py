import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8045547130:AAExrdaRAB3Dsv0WBu-wBpwvdy3moOog7y4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
