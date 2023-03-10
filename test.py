from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
from aiogram import BaseFilter

token: int = ''

bot: Bot = Bot(token=token)
dp: Dispatcher = Dispatcher()


class NumberInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', ' ').replace(',', ' ').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
            if numbers():
                return {'numbers', numbers}
            return False


@dp.message(Text(startswith="numbers", ignore_case=True),
            NumberInMessage())
