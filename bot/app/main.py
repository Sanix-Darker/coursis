from telegram.ext import Updater, CommandHandler, MessageHandler
import json
from bot.app.settings import *
from api.app.utils import *


def presentation():
    print("[+] Coursis-bot started on tg !")

def start_callback(bot, update):
    print("[+] start-callback")

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hello there, what can i search for you"
    )


def echo_callback(bot, update):
    print("[+] echo-callback")

    srch = update.message.text
    results = process(srch, 1)

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hello there, your results for {}({}) !".format(srch, len(results))
    )

    for elt in results:
        response = "----------------------------"
        response += "\n[+] Title: " + elt["title"]
        response += "\n[+] Link: " + elt["url"]
        response += "\n[+] Category: " + elt["category"]
        response += "\n[+] Date: " + elt["date"]

        bot.send_photo(chat_id=update.message.chat_id, photo=elt["img"], caption=response)


def help_callback():
    print("[+] help-callback")

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hello there, you want my help !?"
    )

start_handler = CommandHandler("start", start_callback)
help_handler = CommandHandler("help", help_callback)
echo_handler = MessageHandler(callback=echo_callback, filters=None)


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(echo_handler)


if __name__ == "__main__":
    presentation()

    updater.start_polling()
    updater.idle()
