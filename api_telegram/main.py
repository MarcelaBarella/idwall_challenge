# -*- coding: utf-8 -*-

from telegram import ParseMode
from telegram.ext import (CommandHandler, Updater, MessageHandler, Filters,)
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    """Call to start the bot"""
    update.message.reply_text('Hi! Use /NadaPraFazer <subreddit>;<subreddit> to get your favorite reddit threding topics')

def crawler_caller(bot, update, args):
    """Call the reddit crawler to pass his infos"""   
    try:
        chat_id = update.message.chat_id
        for i in range(len(args)):
            text = "testing args: {}".format(args[0])
        bot.send_message(chat_id, text ,parse_mode=ParseMode.MARKDOWN)
    except (IndexError):
        update.message.reply_text("Please give at most 5 subreddits")


def error(bot, update, error):
    logger.warning("Update {} caused the {} error".format(update, error))

def unreconized_commands(bot, update):
    bot.send_menssage(chat_id=update.message.chat_id, text="""Sorry, I didn't understand your command, 
                        please tipe a valid one""")


def main():
    #omitir do github
    updater = Updater(token='582859019:AAECsrkO6RobYyVb2eV-U31Oz89bzBA6Rxs')
    
    updater_dispatcher = updater.dispatcher

    updater_dispatcher.add_handler(CommandHandler('start', start))
    updater_dispatcher.add_handler(CommandHandler('NadaPraFazer', crawler_caller, pass_args=True))
    
    updater_dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()