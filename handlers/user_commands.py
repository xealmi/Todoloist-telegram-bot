from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from keyboards import reply, inline

router = Router()

@router.message(CommandStart())
async def start(message:Message):
    await message.answer(text='К вашим услугам!', reply_markup=inline.menu)