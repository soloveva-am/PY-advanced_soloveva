

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

PROXY_URL = 'socks5://218.252.244.104' # вставить здесь подходящий ip

secret_token = '2124105320:AAH-xtt84zCPD3_ZgWheAbdNKo0LQniU1FQ'  # строка вида: 123456789:ABCDEFGHJABCDEFGHJABCDEFGHJABCDEFGHJ

bot = Bot(token=secret_token, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)