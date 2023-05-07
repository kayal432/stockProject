from functions import *

add_item,update_item,remove_item,show_item = range(4)

ADD_ITEM, REMOVE_ITEM, UPDATE_ITEM = range(3)

def basic(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Hi {user.first_name}! What would you like to do today?", reply_markup=ReplyKeyboardMarkup([['Add item'], ['Remove item'], ['Update item']], one_time_keyboard=True))
    return ADD_ITEM

def add_item(update, context):
    # Your code for add_item function goes here
    update.message.reply_text("You have chosen to add an item!")
    return ConversationHandler.END

def remove_item(update, context):
    # Your code for remove_item function goes here
    update.message.reply_text("You have chosen to remove an item!")
    return ConversationHandler.END

def update_item(update, context):
    # Your code for update_item function goes here
    update.message.reply_text("You have chosen to update an item!")
    return ConversationHandler.END

def cancel(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Bye {user.first_name}! Hope to see you again soon.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
