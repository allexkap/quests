# Configure logging
import logging
logging.basicConfig(level=logging.INFO)

# Configure environment variables
import os
API_TOKEN = os.getenv('api_token')
CHAT_ID = int(os.getenv('chat_id'))

# Restore usage history (dict)
import pickle
history = pickle.load(open('history.pkl', 'rb'))

# Initialize bot and dispatcher
from aiogram import Bot, Dispatcher, executor, types
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Bot response pattern
@dp.message_handler()
async def echo(message: types.Message):
    chat = message.chat.id
    if chat in history:
        history[chat] += 1
    else:
        history[chat] = 1
    with open('history.pkl', 'wb') as file:
        pickle.dump(history, file)

    await bot.send_message(
        CHAT_ID,
        '#{} @{} ({})'.format(
            history[chat],
            message.from_user.username,
            message.chat.id
        ),
        disable_notification=True
    )
    await bot.forward_message(
        chat_id=CHAT_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        disable_notification=True
    )

    if message.text == '/start':
        await message.answer('floor pow region')
    elif message.text == f'{4 ** 47}':
        await bot.send_message(CHAT_ID, 'perfect')
        await message.reply('perfect')
        await message.answer('please wait')


if __name__ == '__main__':
    executor.start_polling(dp)
