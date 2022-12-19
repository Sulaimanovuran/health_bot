from aiogram import types
from aiogram import Bot
from aiogram.types import ParseMode
from aiogram.dispatcher import Dispatcher

from .config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Связаться с оператором"),
            types.KeyboardButton(text="ИИ"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )
    img_url='https://images.everydayhealth.com/homepage/health-topics-2.jpg?sfvrsn=757370ae_2'
    await message.answer(f'Здаравствуйте {message.from_user.first_name} вас приветствует бот от приложения Health.\nHealth - это ваш личный помощник по уходу за здоровьем <a href="{img_url}">.</a>', parse_mode=ParseMode.HTML, reply_markup=keyboard)


@dp.message_handler(content_types=['photo'])
async def photo_handler(message):
    photo = message.photo.pop()
    await photo.download('/home/uran/telebot_health/media/')

