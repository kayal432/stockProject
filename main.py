from telegram.ext import Updater, CommandHandler
import requests


from functions import *

#start command
def start(update,context):
    message=update.message
    chat_id=message.chat_id
    text=message.text
    bot.sendMessage(chat_id=chat_id,text='hoii')
#help command    
def help(update,context):
   update.message.reply_text("hiii,how can i help you")


def fallback(update: Update, context):
    # your fallback handler code here
    message = updater.message
    text = message.text
    chat_id = message.chat_id
    bot.send_message(chat_id=chat_id, text="I'm sorry, I didn't understand that command.")

def main():
    updater = Updater(token=bot_token, use_context=True)

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(MessageHandler(Filters.command, fallback))
    updater.start_polling()

main()
