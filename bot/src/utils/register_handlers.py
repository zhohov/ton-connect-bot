from aiogram import Dispatcher


async def register_handlers(dp: Dispatcher, handlers: list) -> None:

    for handler in handlers:
        handler(dp)
