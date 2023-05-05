
from functions import *

#start command
def start(update,context):
    message=update.message
    chat_id=message.chat_id
    username=message.from_user.username
    text=message.text
    bot.send_message(chat_id=chat_id, text=f"Hi {username}")
    get = db.reference(f"peoples/{chat_id}").get() or {}
    if chat_id not in get:
        db.reference(f"peoples/{chat_id}").set({
           'chat_id':chat_id,
            'username':username
        })
        bot.send_message(chat_id=chat_id, text=f"Hello new user {username}")
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
 
def command(update,context):
    message = update.message
    chat_id = message.chat_id
    text = message.text
    comm="""/hii\n/help"""
    bot.send_message(chat_id=chat_id, text=comm)
    
    
def main():
    updater = Updater(token=bot_token, use_context=True)

    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('get_command',command))
    dp.add_handler(MessageHandler(Filters.command, fallback))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    updater.start_polling()

main()
