import asyncio
import logging
import json

from telethon import TelegramClient

logging.basicConfig(level=logging.INFO)

api_id = 20276100
api_hash = 'c2fd39c72ef6b2bc3062ec34671435ab'
phone_number = '+998917776365'
group_name = 'ASDiscussiongroup'

client = TelegramClient('comments', api_id, api_hash)
categorised_comments = [
    {
        "type": "Positive Feedback",
        "number": 0,
        "comment_ids": []
    },
    {
        "type": "Negative Feedback",
        "number": 0,
        "comment_ids": []
    },
    {
        "type": "Questions",
        "number": 0,
        "comment_ids": []
    },
    {
        "type": "Suggestions/Advice",
        "number": 0,
        "comment_ids": []
    },
    {
        "type": "Requests for Assistance",
        "number": 0,
        "comment_ids": []
    },
    {
        "type": "General Discussion",
        "number": 0,
        "comment_ids": []
    },
    {
        "type": "Technical Issues",
        "number": 0,
        "comment_ids": []
    },
    {
        "type": "Acknowledgements",
        "number": 0,
        "comment_ids": []
    }
]

final_categorised_comments = [
    {
        "type": "Positive Feedback",
        "number": 0,
        "comments": []
    },
    {
        "type": "Negative Feedback",
        "number": 0,
        "comments": []
    },
    {
        "type": "Questions",
        "number": 0,
        "comments": []
    },
    {
        "type": "Suggestions/Advice",
        "number": 0,
        "comments": []
    },
    {
        "type": "Requests for Assistance",
        "number": 0,
        "comments": []
    },
    {
        "type": "General Discussion",
        "number": 0,
        "comments": []
    },
    {
        "type": "Technical Issues",
        "number": 0,
        "comments": []
    },
    {
        "type": "Acknowledgements",
        "number": 0,
        "comments": []
    }
]

async def comments():
    await client.start(phone_number)
    group = await client.get_entity(group_name)
    comments = []
    async for message in client.iter_messages(group, limit=100):
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
    asyncio.run(comments())
