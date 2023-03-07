# # from aiogram import Bot, Dispatcher
# # from aiogram.filters import Command
# # from aiogram.types import Message
# # from aiogram.types import ContentType
# # from aiogram import F

# # Bot_token: str = '5958065563:AAFhFazb98YVQhoRZkm4t5Ky0x4J-URtsmA'

# # bot: Bot = Bot(token=Bot_token)
# # dp: Dispatcher = Dispatcher()


# # @dp.message(Command(commands=['start']))
# # async def send_command(message: Message):
# #     await message.answer("How do yo do?")


# # @dp.message(Command(commands=['help']))
# # async def send_help(message=Message):
# #     await message.answer('suka blyad')


# # @dp.message(F.photo)
# # async def send_photo(message: Message):
# #     print(message)
# #     await message.reply_photo(message.photo[0].file_id)


# # @dp.message(F.sticker)
# # async def send_sticker(message: Message):
# #     print(message.json())
# #     await message.reply_sticker(message.sticker.file_id)


# # @dp.message(F.voice)
# # async def send_voice(message: Message):
# #     print(message.json())
# #     await message.reply_voice(message.voice.file_id)


# # @dp.message(F.video)
# # async def send_video(message: Message):
# #     print(message.json())
# #     await message.reply_video(message.video.file_id)


# # @dp.message(F.animation)
# # async def echo_animation(message: Message):
# #     print(message.json())
# #     await message.reply_animation(message.animation.file_id)


# # @dp.message()
# # async def echo_answer(message: Message):
# #     await message.reply(text=message.chat.first_name + ', ' + message.text)


# # if __name__ == '__main__':
# #     dp.run_polling(bot)


# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command
# from aiogram.types import Message, ContentType


# bot: int = ('5958065563:AAFhFazb98YVQhoRZkm4t5Ky0x4J-URtsmA')
# dp: Dispatcher = Dispatcher()

# Token: Bot = Bot(token=bot)


# @dp.message(Command(commands=['start']))
# async def send_start(message: Message):
#     await message.answer("Idi naxui")


# @dp.message(Command(commands='help'))
# async def echo_help(message: Message):
#     await message.reply('Suka Blyad')


# @dp.message()
# async def send_copy(message: Message):
#     await message.send_copy(chat_id=message.chat.id)


# if __name__ == '__main__':
#     dp.run_polling(Token)

import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType

token: str = ('5958065563:AAEP6ROf88m3-T4kU1_UnfaWatk8FInmsoE')

dp: Dispatcher = Dispatcher()
bot: Bot = Bot(token=token)

Attempts: int = 5

user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0,
              }


def get_random_number() -> int:
    return random.randint(1, 100)


@dp.message(Command(commands=['start']))
async def answer_start(message: Message):
    await message.answer("Привіт! \nДавай зіграємо у гру 'Вгадай число'?\n"
                         "Щоб отримати правила гри і список доступних"
                         "команд - відправ команду /help")


@dp.message(Command(commands=['help']))
async def answer_help(message: Message):
    await message.answer(f"Правила гри:\n\nЯ загадую число від 1 до 100, "
                         f"а тобі потрібно його вгадати. У вас є {Attempts} спроб.\n\n"
                         f"Доступні команди:\n"
                         f"/help - правила гри та список команд;\n"
                         f"/cancel - вийти з гри;\n"
                         f"/stat - отримати статистику;\n\n"
                         f"Починаємо?")


@dp.message(Command(commands=['stat']))
async def count_stat(message: Message):
    await message.answer(f"Всього ігор зірано: {user['total_games']}\n"
                         f"З них перемог: {user['wins']}")


@dp.message(Command(commands=['cancel']))
async def exit_game(message: Message):
    if user["in_game"]:
        await message.answer(f"Ви вийшли з гри.\n"
                             f"Якщо хочете повернутись - напишіть нам")
        user["in_game"] = False
    else:
        await message.answer(f"Ви шо, того?.\n"
                             f"Ми ж наче і так граємо з вами:)")


@dp.message(Text(text=['Так', 'Давай', 'Вперед', 'Зіграємо', 'Гра'],
                 ignore_case=False))
async def start_game(message: Message):
    if not user["in_game"]:
        await message.answer(f"Добре, я загадав число від 0 до 100\n"
                             f"Твоя задача - вгадати")
        user["in_game"] = True
        user["secret_number"] = get_random_number()
        user["attempts"] = Attempts
    else:
        await message.answer(f"Поки ми граємо, я можу отримувати лише цифри від 0 до 100,"
                             f"а також команди /cancel и /stop :( ")


@dp.message(Text(text=['Ні', 'Не хочу', 'Не треба', 'Не буду', 'Та нє', 'Ніт',], ignore_case=True))
async def finish_game(message: Message):
    if not user["in_game"]:
        await message.answer(f"Добре, закінчуємо. Твоя взяла:(")
    else:
        await message.answer(f"Так ти ми вже граємо , кмон")


@dp.message(lambda x: x.text and x.text.isdigit() and 0 <= int(x.text) <= 100)
async def process_number(message: Message):
    if user["in_game"]:
        if int(message.text) == user["secret_number"]:
            await message.answer("Ого, вгадав!! Це і справді " + message.text + "Зіграємо знову?")
            user["in_game"] = False
            user["wins"] += 1
            user["total_games"] += 1
        if int(message.text) > user["secret_number"]:
            await message.answer("Нє, переборщив. Це менше ніж " + message.text)
            user["attempts"] -= 1
        if int(message.text) < user["secret_number"]:
            await message.answer("Нє, переменшив. Це більше ніж " + message.text)
            user["attempts"] -= 1
        if user["attempts"] == 0:
            await message.answer(f"На жаль, кількість спроб вичерпано.\n\n"
                                 f"Моє число було {user['secret_number']} \n"
                                 f"Зіграємо ще?")
            user["in_game"] = False
            user["total_games"] += 1
    else:
        await message.answer("Ми ще не почали. Хочете почати?")


@dp.message()
async def asking_questions(message: Message):
    if user["in_game"]:
        await message.answer("Цифри, брате чи сестро. Розумію лише цифри!")
    else:
        await message.answer("Merci boku? Не розуміем по польскі")

if __name__ == '__main__':
    dp.run_polling(bot)
