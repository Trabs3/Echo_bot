from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

Bot_token: str = '5958065563:AAFhFazb98YVQhoRZkm4t5Ky0x4J-URtsmA'

bot: Bot = Bot(token=Bot_token)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def send_command(message: Message):
    await message.answer("How do yo do?")


@dp.message(Command(commands=['help']))
async def send_help(message=Message):
    await message.answer('suka blyad')


@dp.message(F.photo)
async def send_photo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


@dp.message(F.sticker)
async def send_photo(message: Message):
    print(message.json())
    await message.reply_sticker(message.sticker.file_id)


@dp.message(F.voice)
async def send_photo(message: Message):
    print(message.json())
    await message.reply_voice(message.voice.file_id)


@dp.message()
async def echo_answer(message: Message):
    await message.reply(text=message.chat.first_name + ', ' + message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
