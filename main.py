import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import *
from keyboards import greet_kb

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()


@dp.message(Command("key"))
async def keyboard_test(message: types.Message):
    await message.answer("Вот Она!", reply_markup=greet_kb)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Start Message!")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
