from functions import *

add_item,update_item,remove_item,show_item = range(4)

def today_date(update,context):
  now = datetime.now()
  date_str = now.strftime("%Y-%m-%d") # format the date as YYYY-MM-DD
  bot.send_message(chat_id=update.message.chat_id, text=f"The current date is {date_str}")
  
  
def add_item():
   bot.send_message(chat_id=update.message.chat_id, text='hii')
   return update_item

def remove_item():
   bot.send_message(chat_id=update.message.chat_id, text='hii')

def update_item():
   bot.send_message(chat_id=update.message.chat_id, text='hii')
   return remove_item
