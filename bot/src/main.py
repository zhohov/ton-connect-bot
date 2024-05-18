import os
import asyncio
import logging

from typing import NoReturn
from aiogram import Bot, Dispatcher

from utils import start_bot, register_handlers 
from handlers import handlers_list


async def main() -> NoReturn:
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    token=os.getenv("TELEGRAM_TOKEN")
    bot = Bot(token=token)

    await register_handlers(dp=dp, handlers=handlers_list)

    await start_bot(dp=dp, bot=bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.exception(f"Error starting bot: {e}")