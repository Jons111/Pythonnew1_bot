# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from keyboards.default.taqqoslash import tasdiqlash
# from states.forma_holat import Forma
# from loader import dp, bot
#
#
# # Echo bot
# @dp.message_handler(commands='forma')
# async def bot_echo(message: types.Message):
#     await message.answer(text='Ismingizni kiriting!')
#     await Forma.ism_qabul.set()
#
# lugat={}
# @dp.message_handler(state=Forma.ism_qabul)
# async def bot_echo(message: types.Message,state:FSMContext):
#     ism = message.text
#     await state.update_data({'ism':ism})
#     await message.answer(text='Familyangizni kiriting!')
#     await Forma.fam_qabul.set()
#
# @dp.message_handler(state=Forma.fam_qabul)
# async def bot_echo(message: types.Message, state:FSMContext):
#     fam = message.text
#     await state.update_data({'fam': fam})
#     matn = ''
#     data = await state.get_data()
#     ism = data.get('ism')
#     fam = data.get('fam')
#
#     matn += f'Ism: {ism}\n' \
#            f'Familiya {fam}\n'
#     await message.answer(text=matn,reply_markup=tasdiqlash)
#     await Forma.taqqoslash.set()
#
# @dp.message_handler(state=Forma.taqqoslash,text='Orqaga⬅️')
# async def bot_echo(message: types.Message):
#     await message.answer(text='Bekor qilindi')
#
# # @dp.message_handler(state=Forma.taqqoslash,text='Tasdiqlash')
# # async def bot_echo(message: types.Message,state:FSMContext):
# #
# #     username = message.from_user.username
# #
# #     data = await state.get_data()
# #     ism = data.get('ism')
# #     fam = data.get('fam')
# #
# #     matn = f'Ism: {ism}\n' \
# #            f'Familiya {fam}\n'
# #
# #
# #     await bot.send_message(chat_id=1722082854,text=matn)
# #     await state.finish()
#
