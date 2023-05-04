

from functions import *


def start(update,context):
    message=update.message
    chat_id=message.chat_id
    text=message.text
    bot.sendMessage(chat_id=chat_id,text='hoii')

def main():
    updater = Updater(bot_token, use_context=True)

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()

main()
