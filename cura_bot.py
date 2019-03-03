# simple telegram bot

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests

# created event Handler. Constantly polling for new messages
updater = Updater(token="634521747:AAFdi1i8pMIKECEdYBrOvIRdGJNCAtlpWSU")
# add new event handlers
dispatcher = updater.dispatcher


def cura(update):
    req = requests.get("https://github.com/mehremic1/telegram-bot/blob/master/response.json")
    response = req.json()[0]["title"]+"\n" + req.json()[0]["body"]
    update.message.reply_text(response)


dispatcher.add_handler(MessageHandler(Filters.text, cura))

# start polling
updater.start_polling()
updater.idle()
