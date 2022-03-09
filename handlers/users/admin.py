from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state

import states
from keyboards.default.MENU import asosiy
from keyboards.default.tasdiqlash import tasdiqlash
from states.forma_holat import Forma
from aiogram.types import ReplyKeyboardRemove
from loader import dp, bot


# Echo bot
@dp.message_handler(text='Adminga habar yuborish👨‍💻')
async def bot_echo(message: types.Message):
    await message.answer("📍📝 Adminga xabar yozishingiz mumkin.\n\n"
                         "- Reklama:\n"
                         "- Botga qanday o'yin yoki ilova qo'shish:\n"
                         "- Kanalni botga ulash: masalasi bo'yicha yozishingiz mumkin.\n\n"
                         "❗️Hozir yozgan habaringiz to'g'ridan-to'gri bot adminiga uzatiladi👇",reply_markup=ReplyKeyboardRemove())
    await Forma.adminga_murojat.set()

@dp.message_handler(state=Forma.adminga_murojat)
async def bot_echo(message: types.Message, state:FSMContext):
    murojat = message.text
    await state.update_data({'Adminga habar': murojat})
    matn = ''
    data = await state.get_data()
    murojat = data.get('Adminga habar')

    matn += f'❗️ Adminga quyidagi xabarni yubormoqchiman, buning uchun habarni siz yozganligingizni tasdiqlashingzi kerak👇\n\n{murojat}\n'
    await message.answer(text=matn, reply_markup=tasdiqlash)
    await Forma.taqqoslash.set()

@dp.message_handler(state=Forma.taqqoslash,text='Tasdiqlash🔧')
async def bot_echo(message: types.Message,state:FSMContext):

    username = message.from_user.username

    data = await state.get_data()
    murojat = data.get('Adminga habar')

    matn = f'⚜️ {username} dan uzatilgan habar: \n {murojat}'


    await bot.send_message(chat_id=5210340202,text=matn)
    await message.answer("♻️ Xabar muvaffaqiyatli yuborildi, tez orada admin sizga javob beradi.",reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=Forma.taqqoslash,text="Bekor qilish❌")
async def bot_echo(message: types.Message):
    username = message.from_user.username

    matn = f'⚜️ {username} dan bekor qilingan habar bor: \n '
    await bot.send_message(chat_id=5210340202, text=matn)
    await message.answer('🚫Bekor qilindi',reply_markup=asosiy)

