from dotenv import load_dotenv
import os
import asyncio

from src.bot import BotRun

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in .env")

bot = BotRun(BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(bot.run())