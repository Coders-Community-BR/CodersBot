from os import listdir

from discord.ext.commands import Bot

import src.log as log


def load_events(bot: Bot):
    for file in listdir("src/events"):
        if file.endswith('.py'):
            bot.load_extension(f"src.events.{file.replace('.py', '')}")
            log.message(f'Evento carregado "{file}"')
        else:
            if file != '__pycache__':
                log.error(f'o arquivo ou pasta "{file}" não é um evento valido.')
