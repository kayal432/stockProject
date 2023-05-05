# from telegram import *
# from telegram.ext import *
# from telegram.ext import Updater
# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler
import firebase_admin
import requests

from firebase_admin import credentials, db
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Bot
from telegram.ext.filters import Filters


bot_token='6061292744:AAEEurmseHxL4nzKnCr4nQzKHyH16kmq24Y'

bot=Bot(token=bot_token)
