from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime


def log(update: Update, context: ContextTypes):
    file = open('log.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name}', 
               f'{update.effective_user.id}', 
               f'{update.message.text}', 
               f'{datetime.now().strftime("%Y.%m.%d %H:%M:%S")}\n')
    file.close()
