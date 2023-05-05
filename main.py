from telegram.ext import Updater, CommandHandler
import requests


from functions import *


def start(update,context):
    message=update.message
    chat_id=message.chat_id
    text=message.text
    bot.sendMessage(chat_id=chat_id,text='hoii')
    
def hii(update,context):
   update.message.reply_text("hiiiiii")
 

def main():
    updater = Updater(token=bot_token, use_context=True)

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('hii',hii))
    updater.start_polling()

main()
