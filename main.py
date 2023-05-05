
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

# your fallback handler code here

def fallback(update: Updater, context):
    message = update.message
    text = message.text
    chat_id = message.chat_id
    bot.send_message(chat_id=chat_id, text="I'm sorry, I didn't understand that command.")
    
   
def message(update,context):
    message = update.message
    chat_id = message.chat_id
    text = message.text
    bot.send_message(chat_id=chat_id, text=text)
        

def main():
    updater = Updater(token=bot_token, use_context=True)

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(MessageHandler(Filters.command, fallback))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    updater.start_polling()

main()
