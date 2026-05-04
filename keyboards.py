from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🤖 الذكاء الاصطناعي", callback_data="ai")],
        [InlineKeyboardButton(text="🌐 الترجمة", callback_data="translate")],
        [InlineKeyboardButton(text="👤 حسابي", callback_data="profile")]
    ]
)

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📊 الإحصائيات", callback_data="stats")]
    ]
)
