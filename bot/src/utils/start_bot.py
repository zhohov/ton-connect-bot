import logging
from typing import NoReturn

from aiogram import Bot, Dispatcher


async def start_bot(bot: Bot, dp: Dispatcher) -> NoReturn:
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except Exception as e:
        logging.info(f"Error starting bot: {e}")
