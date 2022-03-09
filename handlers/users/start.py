from aiogram import types
from keyboards.default.MENU import asosiy
from loader import dp

@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alekum, {message.from_user.full_name}!\n Siz telegramdagi ilovalar va o'yinlar markazidasiz!",reply_markup=asosiy)
