from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_main=ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("🍴 Меню")
    ],
    [
        KeyboardButton("🛍 Мои заказы")
    ],
    [
        KeyboardButton("✍️ Оставить отзыв"),
        KeyboardButton("⚙️ Настройки")
    ]
],resize_keyboard=True)

lokatsiya=ReplyKeyboardMarkup(keyboard=[
    [
      KeyboardButton("🗺 Мои адреса")
    ],
    [
            KeyboardButton("Отправт 📍 геолокацию",request_location=True),
            KeyboardButton("⬅️ Назад")

    ]
],resize_keyboard=True)

