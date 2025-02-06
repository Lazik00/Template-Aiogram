from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_main import menu_main, lokatsiya
from loader import dp

@dp.message_handler(commands='start')
async def menu(message: types.Message):
    await message.answer_photo(open('skidka.jpg', 'rb'),
                               "🎉 Сделай заказ от 89 000 сум и стань участником акции «1000000 призов от EVOS».Выиграй квартиру, автомобиль KIA, отдых в Дубай и еще 1000000 новогодних призов от EVOS! Подробнее на www.evos.uz/2025")
    await message.answer("Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=lokatsiya)
