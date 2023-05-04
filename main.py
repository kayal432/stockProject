from telegram.ext import Updater, CommandHandler
import requests


from functions import *


def start(update,context):
    message=update.message
    chat_id=message.chat_id
    text=message.text
    bot.sendMessage(chat_id=chat_id,text='hoii')
bot = Bot(token=bot_token)

# The URL of the image you want to use as the bot's profile picture
image_url = 'https://images.app.goo.gl/Qw8S9X19KXJr37FT7'

# Download the image from the URL and save it locally
image_data = requests.get(image_url).content
with open('profile_photo.jpg', 'wb') as f:
    f.write(image_data)

# Set the profile picture using the saved image file
with open('profile_photo.jpg', 'rb') as f:
    bot.set_profile_photo(photo=f)

def main():
    updater = Updater(token=bot_token, use_context=True)

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()

main()
