

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

PROXY_URL = 'socks5://218.252.244.104' # вставить здесь подходящий ip

secret_token = '2124105320:AAH-xtt84zCPD3_ZgWheAbdNKo0LQniU1FQ'  # строка вида: 123456789:ABCDEFGHJABCDEFGHJABCDEFGHJABCDEFGHJ

bot = Bot(token=secret_token)
dp = Dispatcher(bot)
Subjects = {'python': 'Геннадий Федонин', 'Теория вероятностей':"Владимир Булинский", 'матан': 'Трушин Виктор Борисович'}
inline_kb_subjects=InlineKeyboardMarkup()
for subject in Subjects.keys():
    inline_kb_subjects.add(InlineKeyboardButton(subject, callback_data=subject))

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("привет! \n я бот-староста \n чем могу помочь?.")


@dp.message_handler(commands=['prepod'])
async def process_start_command(message: types.Message):
    await message.reply("выбери предмет из списка", reply_markup=inline_kb_subjects)


@dp.callback_query_handler(lambda c: c.data == 'python' )
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, Subjects['python'] )
@dp.callback_query_handler(lambda c: c.data == 'Теория вероятностей' )
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, Subjects['Теория вероятностей'] )
@dp.callback_query_handler(lambda c: c.data == 'матан' )
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, Subjects['матан'] )

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('I can\'t process it yet '+ message.text)


if __name__ == '__main__':
    executor.start_polling(dp)