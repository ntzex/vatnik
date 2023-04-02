import logging
from utils import get_random_row
from random import randint
from origamibot.listener import Listener


class MessageListener(Listener):
    def __init__(self, sql_cursor, bot):
        self.bot = bot
        self.cursor = sql_cursor

    def on_message(self, message):
        if randint(0, 10) == 1:
            random_row = get_random_row(self.cursor)
            self.bot.send_message(message.chat.id,
                                  random_row[0])
