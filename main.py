from telegram.ext import Updater, CommandHandler
import requests


from functions import *


def start(update,context):
    message=update.message
    chat_id=message.chat_id
    text=message.text
    bot.sendMessage(chat_id=chat_id,text='hoii')
bot = Bot(token=bot_token)
photo_url = 'https://images.app.goo.gl/Qw8S9X19KXJr37FT7'

response = requests.get(photo_url)
if response.status_code == 200:
    photo_file = BytesIO(response.content)
    bot.set_profile_photo(photo=photo_file)

def main():
    updater = Updater(token=bot_token, use_context=True)

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()

main()
