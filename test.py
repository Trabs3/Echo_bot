from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text, BaseFilter
from aiogram.types import Message
from aiogram.types import ContentType

# class NumberInMessage(BaseFilter):
#     async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
#         numbers = []
#         for word in message.text.split():
#             normalized_word = word.replace('.', ' ').replace(',', ' ').strip()
#             if normalized_word.isdigit():
#                 numbers.append(int(normalized_word))
#             if numbers():
#                 return {'numbers', numbers}
#             return False


# @dp.message(Text(startswith="numbers", ignore_case=True),
#             NumberInMessage())

token: str = '5958065563:AAEP6ROf88m3-T4kU1_UnfaWatk8FInmsoE'

bot: Bot = Bot(token=token)
dp: Dispatcher = Dispatcher()

# admin_ids: list[int] = [161085054]


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        if numbers:
            return {'numbers': numbers}
        return False


@dp.message(Text(startswith='найди числа', ignore_case=True),
            NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
        text=f'Нашел: {str(", ".join(str(num) for num in numbers))}')


@dp.message(Text(startswith='найди числа', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer(
        text='Не нашел что-то :(')

# def writing_start(message: Message) -> bool:
#     return message.text == '/start'

# @dp.message(writing_start)
# async def answer_start(message: Message) -> str:
#     await message.answer(text='This is command Start')


# @dp.message(F.photo)
# async def reply_text(message: Message):
#     caption = "This is photo"
#     await message.answer_photo(message.photo[0].file_id, caption=caption)


# @dp.message(Text(contains='1', startswith='a'))
# async def answer_text(message: Message):
#     await message.answer(text='This is text')


if __name__ == "__main__":
    dp.run_polling(bot)
