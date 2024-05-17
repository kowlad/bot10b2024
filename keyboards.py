from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

buttons = [
    [KeyboardButton(text='12'), KeyboardButton(text='2')],
    [KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'), KeyboardButton(text='6')],
    [KeyboardButton(text='7')],
    [KeyboardButton(text='8'), KeyboardButton(text='9'),KeyboardButton(text='10')],
]
greet_kb = ReplyKeyboardMarkup(keyboard=buttons,
                               resize_keyboard=True,
                               one_time_keyboard=True)