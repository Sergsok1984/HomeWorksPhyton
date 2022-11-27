from telegram import Update
from telegram.ext import ContextTypes
from logger import *
import functions


async def start_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!\n'
                                    f'Это программа сложения двух многочленов.\n'
                                    f'Введите /help для помощи \n')


async def help_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'/start - Начало работы\n'
                                    f'/help - Список команд\n'
                                    f'/instruction - Инструкция\n'
                                    f'/sum - сложение многочленов')


async def instruction_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Инструкция: \n'
                                    f'Введите два полинома разделенных между собой пробелом.\n' 
                                    f'Полином записывается без пробелов.\n'
                                    f'Знак умножения не ставится, возведение в степень - симовл "^".\n'
                                    f'Пример записи многочлена: 3x^2+2x+1=0')


async def sum_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Введите два многочлена разделенных пробелом')

async def sum(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text     
    lst1 = functions.calc_mn([msg.split()[0]])
    lst2 = functions.calc_mn([msg.split()[1]])    
    result = functions.result(lst1, lst2)    
    await update.message.reply_text(f'Cумма многочленов: {result}')    
    
    
   
