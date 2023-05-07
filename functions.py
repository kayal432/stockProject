# from telegram import *
# from telegram.ext import *
# from telegram.ext import Updater
# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler
import firebase_admin
import requests

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    CallbackContext,
    ConversationHandler,
    MessageHandler,
    Filters,
)
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from firebase_admin import credentials, db
from telegram.ext import ConversationHandler
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Bot
from telegram.ext.filters import Filters

cred = credentials.Certificate("stockproject-29f5e-firebase-adminsdk-evs2d-7fa10d62ef.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://stockproject-29f5e-default-rtdb.firebaseio.com/"
})


bot_token='6061292744:AAEEurmseHxL4nzKnCr4nQzKHyH16kmq24Y'

bot=Bot(token=bot_token)
