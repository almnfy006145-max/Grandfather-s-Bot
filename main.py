import asyncio

from aiogram import Bot, Dispatcher

from config import "8729773020:AAGyz9LcsAPKvu2loCl_x1u6ao0w3IvChP4" 
from handlers.start import router as start_router
from handlers.admin import router as admin_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(admin_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
