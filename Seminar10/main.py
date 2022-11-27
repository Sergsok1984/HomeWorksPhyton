from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot_commands import *

app = ApplicationBuilder().token("5738069177:AAGKSg-G9UGZ5piacaY_Dqj3Ma4vxTN-m-E").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("instruction", instruction_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, sum))

print('server start')
app.run_polling()