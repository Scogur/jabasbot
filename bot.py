import time
import logging


from aiogram import Bot, Dispatcher, executor, types


from config import TOKEN
from files import whatId
bot = Bot(token=TOKEN)
dp = Dispatcher(bot = bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Hello, to get video use command /vid + file name \n For example /vid test")
    print(f"user_id={user_id} user_name={user_full_name}")

@dp.message_handler(commands='vid')
async def process_vid(message: types.Message):
    await bot.send_video(message.from_user.id, whatId(message.get_args()))


if __name__ == '__main__':
    executor.start_polling(dp)