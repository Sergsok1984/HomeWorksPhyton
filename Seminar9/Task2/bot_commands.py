from telegram import Update
from telegram.ext import ContextTypes
from logger import *
import functions


async def start_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!\n'
                                    f'Введите /help для помощи\n')


async def help_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'/start - Начало работы\n'
                                    f'/help - Список команд\n'
                                    f'/calc <арифметическое выражение без пробелов>  - Калькулятор')


async def calc_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text   
    result = functions.date(msg.split()[1])    
    await update.message.reply_text(f'{msg.split()[1]} = {result[0]}')