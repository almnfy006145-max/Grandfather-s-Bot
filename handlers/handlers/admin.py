from aiogram import Router, F
from aiogram.types import CallbackQuery

from config import ADMIN_ID
from database import get_users_count

router = Router()

@router.callback_query(F.data == "stats")
async def stats_handler(callback: CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        return await callback.answer("غير مصرح لك", show_alert=True)

    users = get_users_count()

    await callback.message.answer(
        f"📊 عدد المستخدمين:\n{users}"
    )
