#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import subprocess

from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "TELEGRAM_BOT_TOKEN"
AUTHORIZED_USERS = []


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def execute_command(cmd, returns=False):
    result = subprocess.Popen(cmd, shell=True,)
    output, err = result.communicate()
    if result.returncode is 0:
        if returns:
            return output
    else:
        print(err)
        print(result.returncode)
        print(output)
        raise IOError


def start_spotify_client(bot, update, args):

    if update.message.from_user.id not in AUTHORIZED_USERS:
        bot.sendMessage(update.message.chat_id, text='Get the fuck out of here ' + str(update.message.from_user.id))
        return

    try:
        execute_command("sudo kill -INT $(ps auxww | grep '[0-9] python main.py --username ' | awk '{print $2}') &>/dev/null")
        execute_command("sleep 5")
        execute_command("bash /home/osmc/telegram_spotify/scripts/run-spotify-" + str(update.message.from_user.id) + ".sh &")
        bot.sendMessage(chat_id=update.message.chat_id, text="Spotify client is running")
    except Exception as e:
        bot.sendMessage(chat_id=update.message.chat_id, text="Ups, Spotify client didn't started: " + str(e))


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    add_torrent_handler = CommandHandler('start', start_spotify_client, pass_args=True)
    dp.add_handler(add_torrent_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
