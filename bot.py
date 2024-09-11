from database import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import BoundFilter


class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPER_GROUP
        )


API_TOKEN = "6986327120:AAGLdMZWXxpcVwUjNdj2MO4u8aa4rQh-Vq4"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.filters_factory.bind(IsGroup)
create_users_database()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    insert_new_user(user_id)
    await message.answer("First of all add this bot to your discussions group and promote it to admin. Then send command /my_group in group chat. This is all you need to do!")


@dp.message_handler(IsGroup(), commands=['my_group'])
async def my_group(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    connect_user_group(user_id, -chat_id)
    create_chat_database(-chat_id)
    await message.answer(f"""Group is successfully connected to your account!""")
    await message.delete()


@dp.message_handler(IsGroup())
async def my_group(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_id = message.message_id
    time = int(message.date.timestamp())
    comment = message.text
    link =message.url
    insert_group_message(-chat_id, user_id, message_id, time, comment, link)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)