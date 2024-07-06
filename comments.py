import asyncio
import logging
import json

from telethon import TelegramClient

logging.basicConfig(level=logging.INFO)

api_id = 20276100
api_hash = 'c2fd39c72ef6b2bc3062ec34671435ab'
phone_number = '+998917776365'
group_name = 'ASDiscussiongroup'
message_id = 838363

client = TelegramClient('comments', api_id, api_hash)


async def main():
    await client.start(phone_number)
    group = await client.get_entity(group_name)
    comments = []
    async for message in client.iter_messages(group, limit=1000):
        try:
            if message.reply_to:
                comments.append({
                    'user_id': message.from_id.user_id,
                    'message_id': message.id,
                    'time': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'comment': message.text,
                    'reply_to': message.reply_to.reply_to_msg_id
                })
            else:
                comments.append({
                    'user_id': message.from_id.user_id,
                    'message_id': message.id,
                    'time': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'comment': message.text,
                    'reply_to': None
                })
        except:
                pass

    with open('comments.json', 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    asyncio.run(main())
