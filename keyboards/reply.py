from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    KeyboardButtonPollType
    )

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Задачи')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)

tasks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Удалить задачу'),
            KeyboardButton(text='Добавить задачу')   
        ],
        [
            KeyboardButton(text = 'Назад')
        ]
    ],
    resize_keyboard=True,
    selective = True
)