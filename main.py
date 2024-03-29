from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from parser import studentSchedule


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Hi!")


@dp.message_handler(commands=["schedule"])
async def command_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, studentSchedule())


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)
