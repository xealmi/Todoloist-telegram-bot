from aiogram.fsm.state import State, StatesGroup

class delete_list(StatesGroup):
    task = State()

class add_list(StatesGroup):
    task = State()