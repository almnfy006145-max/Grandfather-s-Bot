from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import add_user
from keyboards import main_keyboard

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    )

    await message.answer(
        "مرحباً بك في البوت الاحترافي 🚀\nاضغط أحد الأزرار للبدء:",
        reply_markup=main_keyboard
    )
