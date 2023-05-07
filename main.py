
from functions import *
from basic import *
from scrapmain import *

#start command
def start(update,context):
    message=update.message
    chat_id=message.chat_id
    username=message.from_user.username
    text=message.text
    bot.send_message(chat_id=chat_id, text=f"Hi {username}")
    get = db.reference(f"peoples/{chat_id}").get() or {}
    if len(get)<=0:
        db.reference(f"peoples/{chat_id}").set({
           'chat_id':chat_id,
            'username':username
        })
        bot.send_message(chat_id=chat_id, text=f"Hello new user {username}")
    else:
        reply_keyboard = [["Show Portfolio"]]
    bot.sendMessage(chat_id=chat_id, text="Choose options",
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True),
                    reply_to_message_id=update.message.message_id)
#help command    
def help(update,context):
   update.message.reply_text("hiii,how can i help you")
def portfolio(update,context):
    message=update.message
    chat_id=message.chat_id
    username=message.from_user.username
    text=message.text
    reply_keyboard = [["Basic","Cancel"]]
    bot.sendMessage(chat_id=chat_id, text="Choose options",
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True),
                    reply_to_message_id=update.message.message_id)
# your fallback handler code here

def fallback(update: Updater, context):
    message = update.message
    text = message.text
    chat_id = message.chat_id
    bot.send_message(chat_id=chat_id, text="I'm sorry, I didn't understand that "+text)
    
   
def message(update,context):
    message = update.message
    chat_id = message.chat_id
    text = message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm sorry, I don't understand that  "+text)
    #bot.send_message(chat_id=chat_id, text=text)
 
def command(update,context):
    message = update.message
    chat_id = message.chat_id
    text = message.text
    comm="""/hii\n/help"""
    bot.send_message(chat_id=chat_id, text=comm)

    
    
def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    basic = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('Date of The Day'),today_date)],
        states={
            add_item: [MessageHandler(Filters.text,add_item )],
            update_item: [MessageHandler(Filters.text,update_item)],
            remove_item: [MessageHandler(Filters.text,remove_item)],
        }, fallbacks=[MessageHandler(Filters.regex('^Cancel$'), cancel)]
    )

   
#     dp.add_handler(edit_task_con)
#     dp.add_handler(upi)
#     dp.add_handler(create)
#     dp.add_handler(binance)
#     dp.add_handler(discord)
    dp.add_handler(basic)
    dp.add_handler(CommandHandler(['cancel','start'],start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('get_command',command))
    dp.add_handler(ConversationHandler(Filters.regex('^Basic$'),basic))
    dp.add_handler(MessageHandler(Filters.regex('^Show Portfolio$'),portfolio))
    dp.add_handler(MessageHandler(Filters.command, fallback))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    updater.start_polling()

main()
