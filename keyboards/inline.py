from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, callback_query
from callbacks import menu
menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Задачи', callback_data="задачи")
        ]
    ]
)