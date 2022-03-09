# import wikipedia
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from states.forma_holat import Forma
#
# from loader import dp
# wikipedia.set_lang('uz')
#
# @dp.message_handler(text='Wikipedia Maqola')
# async def bot_echo(message: types.Message):
#     await message.answer(text='Maqola uchun sarlavha kiriting:')
#     await Forma.wikipedia.set()
#
# @dp.message_handler(state=Forma.wikipedia)
# async def bot_echo(message: types.Message,state:FSMContext):
#     try:
#         repsond = wikipedia.summary(message.text)
#         await message.answer(repsond)
#     except:
#         await message.answer("Siz izlagan maqola mavjud emas")