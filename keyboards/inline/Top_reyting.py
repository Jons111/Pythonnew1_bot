from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

oyin_reyting = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1',callback_data='oyr1'),
            InlineKeyboardButton(text='2', callback_data='oyr2'),
            InlineKeyboardButton(text='3',callback_data='oyr3'),
            InlineKeyboardButton(text='4', callback_data='oyr4'),
            InlineKeyboardButton(text='5', callback_data='oyr5')
        ],
    ]
)

ilova_reyting = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='ir1'),
            InlineKeyboardButton(text='2', callback_data='ir2'),
            InlineKeyboardButton(text='3', callback_data='ir3'),
            InlineKeyboardButton(text='4', callback_data='ir4'),
            InlineKeyboardButton(text='5', callback_data='ir5')
        ],

    ]
)