from utils import connect_to_db
from os import getenv
from origamibot import OrigamiBot as Bot
from commands import BotsCommands
from listener import MessageListener

if __name__ == '__main__':
    connection, cursor = connect_to_db(getenv("path_to_db"))
    bot = Bot(getenv("token"))
    bot.add_listener(MessageListener(cursor, bot))
    bot.add_commands(BotsCommands(cursor, bot))
    bot.start()

    while True:
        pass
