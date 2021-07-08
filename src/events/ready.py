from discord.ext.commands import Bot

import src.log as log


def setup(bot: Bot):
    @bot.event
    async def on_ready():
        log.message('eu estou pronto!')
