from aiogram import Router, F
from aiogram.types import CallbackQuery
from data.subloader import get_json
from keyboards.reply import tasks

router = Router()

@router.callback_query()
async def tasks_list(callback: CallbackQuery):
    if callback.data == 'задачи':
            todol = await get_json('data.json')
            if str(callback.from_user.id) not in todol or todol[str(callback.from_user.id)] ==[]:
                ans = 'Тут пусто :('
            else:
                todol = todol[str(callback.from_user.id)]
                todol = [str(str(a+1)+')'+i+'\n') for a,i in enumerate(todol)]
                ans = ''
                ans = ans.join(todol)
            await callback.message.answer(text=f'Ваши задачи:\n{ans}', reply_markup=tasks)
        