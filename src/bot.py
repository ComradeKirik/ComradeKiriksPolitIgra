from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import CommandStart
from aiogram.types import Message

from handlers.start_handler import router
import asyncio


class BotRun:
    def __init__(self, token: str):
        session = AiohttpSession(proxy="socks5://localhost:8080")
        self.bot = Bot(token=token, session=session)
        self.dp = Dispatcher()

    def _register_handlers(self):
        self.dp.include_router(router)

    async def run(self):
        self._register_handlers()
        await self.dp.start_polling(self.bot)