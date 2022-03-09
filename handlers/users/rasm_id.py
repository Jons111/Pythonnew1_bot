# from aiogram import types
# from aiogram.types import ContentType
#
# from loader import dp
#
#
# # Echo bot
# @dp.message_handler(content_types=ContentType.PHOTO)
# async def bot_echo(message: types.Message):
#     await message.photo[0].download()
#     rasm_id = message.photo[1].file_id
#     await message.answer(text=rasm_id)
#
# @dp.message_handler(content_types=ContentType.DOCUMENT)
# async def bot_echo(message: types.Message):
#     await message.document.download()
#     game_id = message.document.file_id
#     await message.answer(text=game_id)
#
#
#
