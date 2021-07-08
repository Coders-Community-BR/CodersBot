from os import getenv

from discord.ext import commands
from dotenv import load_dotenv

from src.handlers import event, command
from src.log import message, error

message('CodersBot by CodersCommunity')
if __name__ == '__main__':
    error('Por favor rode o arquivo main.py.')
    exit(1)


class CodersBot:

    def __init__(self):
        load_dotenv()
        self.bot = commands.Bot(command_prefix=getenv('DISCORD_PREFIX'))
        event.load_events(self.bot)
        command.load_commands(self.bot)

    def run(self):
        self.bot.run(getenv('DISCORD_TOKEN'))
