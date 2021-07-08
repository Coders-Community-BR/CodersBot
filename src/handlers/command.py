from os import listdir

from discord.ext.commands import Bot

import src.log as log


def load_commands(bot: Bot):
    for pasta in listdir('src/commands'):
        for arquivo in listdir(f'src/commands/{pasta}'):
            if arquivo.endswith('.py'):
                bot.load_extension(f'src.commands.{pasta}.{arquivo.replace(".py", "")}')
                log.message(f'comando carregado "commands.{pasta}.{arquivo.replace(".py", "")}"')
