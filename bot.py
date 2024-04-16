from aiogram import Bot, Dispatcher
import asyncio
from handlers import bot_messages, user_commands
from config_reader import config
from callbacks import menu

async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        menu.router,
        bot_messages.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())