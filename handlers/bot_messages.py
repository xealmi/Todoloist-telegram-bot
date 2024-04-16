from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data.subloader import get_json
from keyboards import inline
from keyboards.reply import tasks
from utils.states import delete_list, add_list
import json

router = Router()

@router.message(F.text.lower() == 'задачи')
async def todolist(message:Message):
    todol = await get_json('data.json')
    if str(message.from_user.id) not in todol or todol[str(message.from_user.id)] ==[]:
        ans = 'Тут пусто :('
    else:
        todol = todol[str(message.from_user.id)]
        todol = [str(str(a+1)+')'+i+'\n') for a,i in enumerate(todol)]
        ans = ''.join(todol)
    await message.answer(text=f'Ваши задачи:\n{ans}', reply_markup=tasks)

@router.message(F.text.lower() == 'удалить задачу')
async def delete_task(message:Message, state: FSMContext):
    await message.answer(text='Какую задачу Вы хотите удалить?')
    await state.set_state(delete_list.task)

@router.message(delete_list.task)
async def delete__(message: Message, state:FSMContext):
    if message.text.isdigit():
        await state.update_data(task = int(message.text))
        todol = await get_json('data.json')
        todol2 = todol[str(message.from_user.id)]
        task = await state.get_data()
        await state.clear()
        task = task["task"]
        if 0 < task <=len(todol2):
            del todol2[task-1]
            todol[str(message.from_user.id)] = todol2
            with open('data/data.json', 'w', encoding='utf-8') as file:
                json.dump(todol, file, indent = 4, ensure_ascii=False)
            if str(message.from_user.id) not in todol or todol[str(message.from_user.id)] ==[]:
                ans = 'Тут пусто :('
            else:
                todol = todol[str(message.from_user.id)]
                todol = [str(str(a+1)+')'+i+'\n') for a,i in enumerate(todol)]
                ans = ''.join(todol)
            await message.answer(text=f'Задача успешно удалена!\nВаши задачи:\n{ans}', reply_markup=tasks)
        else: 
            await message.answer(text='Такой задачи нет!')
    else: 
        await message.answer(text='Такой задачи нет!')

@router.message(F.text.lower() == 'добавить задачу')
async def add_task(message: Message, state: FSMContext):
    await message.answer(text='Какую задачу вы хотите добавить?')
    await state.set_state(add_list.task)

@router.message(add_list.task)
async def add_task(message: Message, state: FSMContext):
    await state.update_data(task = message.text)
    todol =  await get_json('data.json')
    data = await state.get_data()
    await state.clear()
    data = data["task"]
    todol[str(message.from_user.id)].append(data)
    with open ('data/data.json', 'w', encoding='utf-8') as file:
        json.dump(todol, file, indent=4, ensure_ascii=False)
    todol = [str(str(a+1)+')'+i+'\n') for a,i in enumerate(todol[str(message.from_user.id)])]
    ans = ''.join(todol)
    await message.answer(text=f'Задача успешно добавлена!\nВаши задачи:\n{ans}', reply_markup=tasks)

@router.message(F.text.lower() == 'назад')
async def back(message: Message):
    await message.answer(text='К вашим услугам!', reply_markup=inline.menu)