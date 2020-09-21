from telegram.ext import(
    Updater,
    CommandHandler,
    MessageHandler,
    PrefixHandler,
    Filters
)

from lib import tclasses
import os
import random


USER_TOKEN = "973015144:AAGpR9uAwPd3uTa-zaNo-WUcHHZf7uV0ZO8"


start = tclasses.handler()
save_file = tclasses.handler()
read_file = tclasses.handler()
message = tclasses.handler()
add_file = tclasses.handler()

def run_bot():
    updater = Updater(USER_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start.start))
    dispatcher.add_handler(PrefixHandler("!", "save", save_file.save_file))
    dispatcher.add_handler(PrefixHandler("!", "read", read_file.read_file))
    dispatcher.add_handler(PrefixHandler("!", "add", add_file.add_file))
    dispatcher.add_handler(MessageHandler(Filters.text, message.message))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run_bot()