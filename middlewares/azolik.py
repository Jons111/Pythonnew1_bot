from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import kanallar
from utils import azolikk
from loader import bot

class Asosiy(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "A'zo bo'l"

        dastlabki_holat= True
        for k in kanallar:
            holat = await azolikk.tekshirish(user_id=user_id,kanal=k)
            dastlabki_holat *= holat

            kanal = await bot.get_chat(k)
            if not holat:
                link = await kanal.edit_invite_link()
                matn += ('<a href=',link,'>',kanal.title,'</a>')


        if not dastlabki_holat:
            await xabar.message.answer(matn,disable_web_page_preview=True,)
            raise CancelHandler()