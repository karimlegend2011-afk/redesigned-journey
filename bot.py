import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("YCPB bot запущен 🚀")

@dp.message(Command("trends"))
async def trends(message: types.Message):
    await message.answer("Я пока учусь анализировать fashion-тренды 😄")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
