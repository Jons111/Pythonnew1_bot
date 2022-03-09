from aiogram import types

from keyboards.default.Dasturlar import oyin, dastur
from keyboards.default.Turkumlar import oyin_t,ilova_t

from loader import dp

#--------KATTA MENU-------#
@dp.message_handler(text="O'yinlar🎮")
async def bot_echo(message: types.Message):
    await message.answer('O\'yinlar sahifasi👇',reply_markup=oyin)

@dp.message_handler(text='Ilovalar📲')
async def bot_echo(message: types.Message):
    await message.answer('Ilovalar sahifasi👇',reply_markup=dastur)

# @dp.message_handler(text="Kitoblar📚")
# async def bot_echo(message: types.Message):
#     await message.answer('Kitoblar sahifasi👇',reply_markup=kitoblar)
#
# @dp.message_handler(text="Filmlar🎥")
# async def bot_echo(message: types.Message):
#     await message.answer("Filmlar sahifasi👇",reply_markup=filmlar)


#-------"O'yinlar🎮"-------#
@dp.message_handler(text='Top reyting')
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/2',caption="✍️Oyin nomi: Speed Motor Dash\n"
                         "🆚Versiya: 2.01\n"
                         "⚙️Kerakli Android Versiyasi: 4.4+\n"
                         "♻️Yangilanish: May 18, 2021\n"
                          "📲Hajmi: 292.23 MB\n"
                          "📕Ulanish: #offline \n"
                          "🎮 Tur:  #poyga #mototsikl #bir_kishilik #uslubiy_grafika \n"
                          "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/3',
                                  caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/4',caption="✍️O'yin nomi: Brawl Stars\n"
                                                                                 "🆚Versiyasi: 42.333\n"
                                                                                 "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                                                                 "♻️Yangilanish: Feb 23, 2021\n"
                                                                                 "📲Hajmi: 343.54 MB\n"
                                                                                 "🏆Reyting (Play Store): 3.5\n"
                                                                                 "📕Ulanish: #online  \n"
                                                                                 "🎮Tur #jangavor #otishmalar #bir_kishilik \n\n"
                                                                                 "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/5',
                                  caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/6',
                                 caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/16',caption="✍️O'yin nomi: Real Gangster Crime\n"
                                                                                  "🆚Versiyasi: 5.7.7\n"
                                                                                  "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                                                                  "♻️Yangilanish: Feb 1, 2021\n"
                                                                                  "📲Hajmi: 97.43 MB\n"
                                                                                  "🏆Reyting (Play Store): 4.1\n"
                                                                                  "📕Ulanish: #offline \n"
                                                                                  "🎮Tur #jangavor #sarguzasht\n\n"
                                                                                  "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/17',caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/18',caption="✍️O'yin nomi: Beat Fire \n"
                                                                                  "🆚Versiya: 1.1.66\n"
                                                                                  "⚙️ Kerakli Android Versiyasi: 4.4+\n"
                                                                                  "♻️Yangilanish: Aug 12, 2021\n"
                                                                                  "📲Hajmi: 38.07 MB\n"
                                                                                  "📕Ulanish: #offline \n"
                                                                                  "🎮 Tur:  #musiqa #abstrak #uslubiy_grafika \n\n"
                                                                                  "📥Hamkor: https://t.me/PlayMarketNew_bot")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/19',
                                 caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/20', caption="✍️O'yin nomi: Special Forces Group 2\n"
                                                                                   "🆚Versiya: 4.2\n"
                                                                                   "♻️Yangilanish: Jan 27, 2021\n"
                                                                                   "📲Hajmi: 343.72MB\n"
                                                                                   "✅Tekshirildi @tekshiruv_pmbot\n"
                                                                                   "📕Ulanish: #offline #online \n"
                                                                                   "🎮 Tur:  #jangovar #otishma #bellashuvli_multiplayer \n"
                                                                                   "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/21', caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/22',
                              caption="✍️O'yin nomi: Pubg Mobile\n"
                                      "🆚Versiya: 1.8.0\n"
                                      "⚙️ Kerakli Android Versiyasi: 5.1+\n"
                                      "♻️Yangilanish: Jan 12, 2022\n"
                                      "📲Hajmi: 682.16 MB\n"
                                      "📕Ulanish: #online \n"
                                      "🎮 Tur:  #jangavor #otishma #juda_tabiiy #multipleyer\n\n"
                                      "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/23',
                                  caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')


@dp.message_handler(text="O'yin turkumlari")
async def bot_echo(message: types.Message):
    await message.answer('Turkumlarni tanlang👇', reply_markup=oyin_t)

@dp.message_handler(text='Bolalar uchun')
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/34',
                              caption="✍️Name:Chef Kids \n"
                                                                                  "🆚️Version: 1.0.3\n"
                                                                                  "♻️Last Updated: Jun 6, 2018\n"
                                                                                  "📲Size: 45.44MB\n"
                                                                                  "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/35',
                                 caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/36',
                              caption="✍️Name:Kids Burger Chef \n"
                                      "🆚️Version: 2.0\n"
                                      "♻️Last Updated: Mar 21, 2019\n"
                                      "📲Size: 42.38MB\n\n"
                                      "📥Hamkor: https://t.me/PlayMarketNew_bot")
    await message.reply_document(document='https://t.me/Play_Marketbot_news/37',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

#-------Ilovalar📲---------#
@dp.message_handler(text='Ilova turkumlari')
async def bot_echo(message: types.Message):
    await message.answer('Turkumlarni tanlang👇', reply_markup=ilova_t)

@dp.message_handler(text='Ilova Top reyting')
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/24', caption="-- ilova nomi: Telegram\n"
                                                                                   "-- versiya: 8.5.4\n"
                                                                                   "-- kerakli android versiyasi: 4.4+\n"
                                                                                   "-- yangilanish: Feb 15, 2021\n"
                                                                                   "-- hajmi: 44.44 MB\n"
                                                                                   "-- tekshirildi: @tekshiruv_pmbot\n"
                                                                                   "-- ulanish: #online \n\n"
                                                                                   "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/25',
                                  caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/26', caption="-- ilova nomi: Instagram\n"
                                                                                   "-- versiya: 217.0.0.1t\n"
                                                                                   "-- kerakli android versiyasi: 4.4+\n"
                                                                                   "-- yangilanish: Jan 10, 2021\n"
                                                                                   "-- hajmi: 44.33 MB\n"
                                                                                   "-- tekshirildi: @tekshiruv_pmbot\n"
                                                                                   "-- ulanish: #online\n"
                                                                                   "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/27',
                                  caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/28', caption="-- ilova nomi: Tik Tok\n"
                                                                                   "-- versiya: 17.4\n"
                                                                                   "-- kerakli android versiyasi: 4.1+\n"
                                                                                   "-- yangilanish: Oct 23, 2020\n"
                                                                                   "-- hajmi:  82.85MB\n"
                                                                                   "-- ulanish: #online\n" 
                                                                                   "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/29',
                                  caption='#orginal,\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/30', caption="-- ilova nomi: WhatsApp Messenger \n"
                                                                                   "-- versiya: 2.21.24.22\n"
                                                                                   "-- kerakli android versiyasi: 4.4+\n"
                                                                                   "-- yangilanish: Dec 10, 2021\n"
                                                                                   "-- hajmi:  46.92 MB\n"
                                                                                   "-- ulanish: #online\n"
                                                                                   "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/31',
                                  caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/32',
                              caption="-- ilova nomi: Snapchat \n"
                                      "-- versiya: 11.56\n"
                                      "-- kerakli android versiyasi: 4.4+\n"
                                      "-- yangilanish: Nov 30, 2021\n"
                                      "-- hajmi:  62.84 MB\n"
                                      "-- ulanish: #online\n"
                                      "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/33',
                                 caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

#--------O'yin turkumlari-------#
@dp.message_handler(text="Jangovor")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/38',caption="✍️O'yin nomi: Real Gangster Crime\n"
                                                                                  "🆚Versiyasi: 5.7.7\n"
                                                                                  "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                                                                  "♻️Yangilanish: Feb 1, 2021\n"
                                                                                  "📲Hajmi: 97.43 MB\n"
                                                                                  "🏆Reyting (Play Store): 4.1\n"
                                                                                  "📕Ulanish: #offline \n"
                                                                                  "🎮Tur #jangavor #sarguzasht\n\n"
                                                                                  "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/39',
                                  caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/40',
                              caption="✍️O'yin nomi: Warlings 2\n"
                                      "🆚Versiyasi: 2.1.1\n"
                                      "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                      "♻️Yangilanish: Feb 28, 2021\n"
                                      "📲Hajmi: 74.52 MB\n"
                                      "🏆Reyting (Play Store): 4.3\n"
                                      "📕Ulanish: #offline \n"
                                      "🎮Tur #jangavor #bir_kishilik #strategiya \n\n"
                                      "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/41',
                                  caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="Poygalar")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/42',caption="✍️O'yin nomi: Zombie Derby\n"
                                                                                  "🆚Versiyasi: 1.0.19\n"
                                                                                  "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                                                                  "♻️Yangilanish: Nov 8, 2021\n"
                                                                                  "📲Hajmi: 55.19 MB\n"
                                                                                  "🏆Reyting (Play Store): 4.4\n"
                                                                                  "📕Ulanish: #offline \n"
                                                                                  "🎮Tur #poygalar #bir_kishilik \n\n"
                                                                                  "📥Hamkor:  https://t.me/PlayMarketNew_bot")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/43',
                                  caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/44',caption="✍️O'yin nomi: Slingshot Stunt Driver\n"
                                                                                  "🆚Versiya: 1.9.14\n"
                                                                                  "⚙️ Kerakli Android Versiyasi: 4.4+\n"
                                                                                  "♻️Yangilanish: Jul 2, 2021\n"
                                                                                  "📲Hajmi: 123.17 MB\n"
                                                                                  "📕Ulanish: #offline \n"
                                                                                  "🎮 Tur:  #poygalar #boshqotirma #fizika #uslubiy_grafika \n\n"
                                                                                  "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document="https://t.me/Play_Marketbot_news/45",
                                  caption='vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="Jumboq")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/46', caption="✍️O'yin nomi: Tiny Robots\n"
                                                                                   "🆚Versiya: 1.21\n"
                                                                                   "⚙️ Kerakli Android Versiyasi: 4.4+\n"
                                                                                   "♻️Yangilanish: Dec 9, 2020\n"
                                                                                   "📲Hajmi: 140.69MB\n"
                                                                                   "📕Ulanish: #offline \n"
                                                                                   "🎮 Tur: #jumboq #bir_kishilik #kazual \n\n"
                                                                                   "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document="https://t.me/Play_Marketbot_news/47",
                                  caption='vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/48', caption="✍️O'yin nomi: DOP 2\n"
                                                                                   "🆚Versiyasi: 1.1.8\n"
                                                                                   "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                                                                   "♻️Yangilanish: Jan 11, 2022\n"
                                                                                   "📲Hajmi: 148.14 MB\n"
                                                                                   "🏆Reyting (Play Store): 4.2\n"
                                                                                   "📕Ulanish: #offline \n"
                                                                                   "🎮Tur #jumboq #bir_kishilik #uslubiy\n\n"
                                                                                   "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document="https://t.me/Play_Marketbot_news/49", caption='vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="Sarguzashtlar")
async def bot_echo(message: types.Message):
    await message.answer('Sarguzasht o\'yinlar')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/50',
                              caption="✍️O'yin nomi: Don't Starve\n"
                                      "🆚Versiyasi: 1.19.5\n"
                                      "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                      "♻️Yangilanish: Mar 1, 2022\n"
                                      "📲Hajmi: 478.07 MB\n"
                                      "🏆Reyting (Play Store): 4.4\n"
                                      "📕Ulanish: #offline \n"
                                      "🎮Tur #sarguzasht #pullik #bir_kishilik \n\n"
                                      "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/51',
                                  caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/52',
                              caption="✍️O'yin nomi: 60 Seconds! Reatomized\n"
                                      "🆚Versiyasi: 1.2.0\n"
                                      "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                      "♻️Yangilanish: Feb 7, 2022\n"
                                      "📲Hajmi: 176.05 MB\n"
                                      "📕Ulanish: #offline\n"
                                      "🎮Tur #sarguzasht \n\n"
                                      "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/53',caption='vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="Boshqalar")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/54',caption="✍️O'yin nomi: Idle Zombie Survival\n"
                                                                                  "🆚Versiyasi: 3.0.0\n"
                                                                                  "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                                                                  "♻️Yangilanish: Feb 28, 2021\n"
                                                                                  "📲Hajmi: 209.91 MB\n"
                                                                                  "🏆Reyting (Play Store): 4.4\n"
                                                                                  "📕Ulanish: #offline \n"
                                                                                  "🎮Tur #boshqalar #uslubiy \n\n"
                                                                                  "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/55',caption='#vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/56',caption="✍️O'yin nomi: Ground Digger\n"
                                                                                  "🆚Versiyasi: 1.24.0\n"
                                                                                  "⚙️ Kerakli Android Versiyasi: 5.0+\n"
                                                                                  "♻️Yangilanish: Feb 25, 2022\n"
                                                                                  "📲Hajmi: 80.64 MB\n"
                                                                                  "🏆Reyting (Play Store): 3.7\n"
                                                                                  "📕Ulanish: #offline \n"
                                                                                  "🎮Tur #boshqalar \n\n"
                                                                                  "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/57',caption='vzlom\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

#--------Ilova turkumlari-------#
@dp.message_handler(text="Ijtimoiy tarmoqlar")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/24', caption="-- ilova nomi: Telegram\n"
                                                                                   "-- versiya: 8.5.4\n"
                                                                                   "-- kerakli android versiyasi: 4.4+\n"
                                                                                   "-- yangilanish: Feb 15, 2021\n"
                                                                                   "-- hajmi: 44.44 MB\n"
                                                                                   "-- tekshirildi: @tekshiruv_pmbot\n"
                                                                                   "-- ulanish: #online \n\n"
                                                                                   "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/25', caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/26', caption="-- ilova nomi: Instagram\n"
                                                                                   "-- versiya: 217.0.0.1t\n"
                                                                                   "-- kerakli android versiyasi: 4.4+\n"
                                                                                   "-- yangilanish: Jan 10, 2021\n"
                                                                                   "-- hajmi: 44.33 MB\n"
                                                                                   "-- tekshirildi: @tekshiruv_pmbot\n"
                                                                                   "-- ulanish: #online\n"
                                                                                   "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/27', caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/28', caption="-- ilova nomi: Tik Tok\n"
                                                                                   "-- versiya: 17.4\n"
                                                                                   "-- kerakli android versiyasi: 4.1+\n"
                                                                                   "-- yangilanish: Oct 23, 2020\n"
                                                                                   "-- hajmi:  82.85MB\n"
                                                                                   "-- ulanish: #online\n"
                                                                                   "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/29', caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/30',
                              caption="-- ilova nomi: WhatsApp Messenger \n"
                                      "-- versiya: 2.21.24.22\n"
                                      "-- kerakli android versiyasi: 4.4+\n"
                                      "-- yangilanish: Dec 10, 2021\n"
                                      "-- hajmi:  46.92 MB\n"
                                      "-- ulanish: #online\n"
                                      "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/31', caption='#orginal\n@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/64',caption='-- Ilova nomi: Likee\n'
                                                                                  '-- Versiya: 3.67.1\n'
                                                                                  '-- Kerakli Android Versiyasi: 4.4+\n'
                                                                                  '-- Yangilanish: Jul 9, 2021\n'
                                                                                  '-- Hajmi:  79.03 MB\n'
                                                                                  '-- Ulanish: #online \n\n'
                                                                                  '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/65',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="Fotografiya")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/58',caption="-- Ilova nomi: Photo Studio\n"
                                                                                  "-- Versiya: 2.5.5.3\n"
                                                                                  "-- Kerakli Android Versiyasi: 4.4+\n"
                                                                                  "-- Yangilanish: Mar 22, 2021\n"
                                                                                  "-- Hajmi: 45.14MB\n"
                                                                                  "-- Ulanish: #offline \n"
                                                                                  "-- Vazifasi: Fotografiya\n"
                                                                                  "\n📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/59',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/60',caption="-- ilova nomi: Fonts Keyboard\n"
                                                                                  "-- versiya: 4.4.3\n"
                                                                                  "-- kerakli android versiyasi: 4.4+\n"
                                                                                  "-- yangilanish: Aug 19, 2021\n"
                                                                                  "-- hajmi: 6.23 MB\n"
                                                                                  "-- ulanish: #offline \n\n"
                                                                                  "📥Kanal: https://t.me/Play_Marketbot_news ")
    await message.answer_document(document="https://t.me/Play_Marketbot_news/61",caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/62',caption="-- ilova nomi: Photo Lab \n"
                                                                                  "-- versiya: 3.12.0\n"
                                                                                  "-- kerakli android versiyasi: 4.4+\n"
                                                                                  "-- yangilanish: Dec 16, 2021\n"
                                                                                  "-- hajmi: 21.19 MB\n"
                                                                                  "-- tekshirildi: @tekshiruv_pmbot\n"
                                                                                  "-- ulanish: #offline \n\n"
                                                                                  "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/63',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/66',caption='-- Ilova nomi: FaceApp \n'
                                                                                   '-- Versiya: 4.5.0.8\n'
                                                                                   '-- Kerakli Android Versiyasi: 4.4+\n'
                                                                                   '-- Yangilanish: Jun 18, 2021\n'
                                                                                   '-- Hajmi: 36.14MB\n'
                                                                                   '-- Ulanish: #offline \n\n'
                                                                                   '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/67',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="Musiqa va audio")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/68',caption='-- Ilova nomi: Shazam\n'
                                                                                   '-- Versiya: 11.25\n'
                                                                                   '-- Kerakli Android Versiyasi: 4.4+\n'
                                                                                   '-- Yangilanish: May 10, 2021\n'
                                                                                   '-- Hajmi: 23.68 MB\n'
                                                                                   '-- Ulanish: #online \n'
                                                                                   '-- Vazifasi: Musiqa qidirish\n\n'
                                                                                   '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/69',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/70',
                               caption='-- Ilova nomi: Dub Music Player\n'
                                       '-- Versiya: 5.3\n'
                                       '-- Kerakli Android Versiyasi: 4.4+\n'
                                       '-- Yangilanish: Nov 17, 2021\n'
                                       '-- Hajmi:  13.18 MB\n'
                                       '-- Ulanish: #offline \n\n'
                                       '📥Kannal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/71',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/72',caption='-- Ilova nomi: Yandex Music\n'
                                                                                  '-- Versiya: 2021.07.2\n'
                                                                                  '-- Kerakli Android Versiyasi: 4.4+\n'
                                                                                  '-- Yangilanish: Jul 7, 2021\n'
                                                                                  '-- Hajmi:  14.09 MB\n'
                                                                                  '-- Ulanish: #online \n\n'
                                                                                  '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/73',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/74',caption="-- Ilova nomi: Music Player\n"
                                                                                   "-- Versiya: 1.4.0\n"
                                                                                   "-- Kerakli Android Versiyasi: 4.0+\n"
                                                                                   "-- Yangilanish: Sep 25, 2019\n"
                                                                                   "-- Hajmi:  9.92 MB\n"
                                                                                   "-- Ulanish: #offline \n\n"
                                                                                   "📥Kanal: https://t.me/Play_Marketbot_news")
    await message.answer_document(document='https://t.me/Play_Marketbot_news/75',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="Video pleyer va muharrirlar")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/76',caption='-- ilova nomi: Collage Maker\n'
                                                                                   '-- versiya: 1.341\n'
                                                                                   '-- kerakli android versiyasi: 4.4+\n'
                                                                                   '-- yangilanish: Nov 29, 2021\n'
                                                                                   '-- hajmi: 21.39 MB\n'
                                                                                   '-- ulanish: #offline \n\n '
                                                                                   '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/77',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/78',
                               caption='-- ilova nomi: InShot Video Editor\n'
                                       '-- versiya: 1.780.1344\n'
                                       '-- kerakli android versiyasi: 4.4+\n'
                                       '-- yangilanish: Dec 25, 2021\n'
                                       '-- hajmi: 68.87 MB\n'
                                       '-- ulanish: #offline\n\n'
                                       '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/79', caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/80',caption='-- Ilova nomi: Funimate Video Editor\n'
                                                                                   '-- Versiya: 11.14\n'
                                                                                   '-- Kerakli Android Versiyasi: 4.4+\n'
                                                                                   '-- Yangilanish: Aug 26, 2021\n'
                                                                                   '-- Hajmi: 193.62 MB\n'
                                                                                   '-- Ulanish: #online \n\n'
                                                                                   '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/81',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')

@dp.message_handler(text="BoshqaIar")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/82',caption='✍️Ilova nomi: Video Downloader for Instagram\n'
                                                                                   '🆚Versiya: 6.0.20\n'
                                                                                   '⚙️ Kerakli Android Versiyasi: 5+\n'
                                                                                   '♻️Yangilanish: Jan 9, 2021\n'
                                                                                   '📲Hajmi: 5.9MB\n'
                                                                                   '📕Ulanish: #online\n\n'
                                                                                   '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/83',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/84',
                               caption='-- ilova nomi: Powerful Cleaner pro\n'
                                       '-- versiya: 1.0.20\n'
                                       '-- kerakli android versiyasi: 4.4+\n'
                                       '-- yangilanish: Feb 9, 2022\n'
                                       '-- hajmi: 7.42 MB\n'
                                       '-- ulanish: #offline \n'
                                       '\n📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/85',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')
    await message.answer_photo(photo='https://t.me/Play_Marketbot_news/86',
                               caption='-- ilova nomi: Kaspersky Security & VPN\n'
                                       '-- versiya: 11.81.4\n'
                                       '-- kerakli android versiyasi: 4.4+\n'
                                       '-- yangilanish: Jan 26, 2021\n'
                                       '-- hajmi: 65.97 MB\n'
                                       '-- ulanish: #offline \n\n'
                                       '📥Kanal: https://t.me/Play_Marketbot_news')
    await message.answer_document(document='https://t.me/Play_Marketbot_news/87',caption='@PlayMarketNew_bot | Siz tanlagan yagona o\'yinlar va ilovalar markazi😅👌')



