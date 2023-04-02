from utils import get_random_row


class BotsCommands:
    def __init__(self, sql_cursor, bot):
        self.bot = bot
        self.cursor = sql_cursor

    def start(self, message):
        self.bot.send_message(message.chat.id, "Привет, я ватник.")

    def mrand(self, message):
        random_row = get_random_row(self.cursor)
        self.bot.send_message(message.chat.id,
                              f"{random_row[0]}\n©️ {random_row[3]}")
