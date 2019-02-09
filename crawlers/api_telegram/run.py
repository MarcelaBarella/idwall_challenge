# -*- coding: utf-8 -*-
import os
import time

from telegram import ParseMode
from telegram.ext import (CommandHandler, Updater, MessageHandler, Filters)
import logging

from reddit_crawler import RedditCrawler
import utils

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    """Call to start the bot"""
    update.message.reply_text('Hi! Use /NadaPraFazer <subreddit>;<subreddit> to get your favorite reddit threading topics')

def crawler_caller(bot, update, args):
    if not args:
        update.message.reply_text("Please give at least 1 subreddit")
        return

    crawler = RedditCrawler()
    subreddits = args[0].split(';')
    threads = []

    for subreddit in subreddits:
        time.sleep(2) #in respect to limit imposed by reddit to developers
        threads.extend(crawler.get_threads(subreddit)[:5])

    formatted_threads = map(lambda t: t.to_markdown(), threads)

    text = "\n  -------------  \n".join(formatted_threads)

    try:
        chat_id = update.message.chat_id
        bot.send_message(chat_id, text ,parse_mode=ParseMode.MARKDOWN)
    except Exception as err:
        print(err)
        update.message.reply_text(
            "Whoops! Something went wrong. Sometimes Reddit blocks me or your " + \
            "reddit search has given no results. Please, wait a few (or a lot) " +\
            "seconds and try again later")


def error(bot, update, error):
    logger.warning("Update {} caused the {} error".format(update, error))

def unreconized_commands(bot, update):
    bot.send_menssage(chat_id=update.message.chat_id, text="""Sorry, I didn't understand your command, 
                        please tipe a valid one""")


def main():

    updater = Updater(token=os.environ['TELEGRAM_BOT_TOKEN'])
    
    updater_dispatcher = updater.dispatcher

    updater_dispatcher.add_handler(CommandHandler('start', start))
    updater_dispatcher.add_handler(CommandHandler('NadaPraFazer', crawler_caller, pass_args=True))
    
    updater_dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()