from discord.ext.commands import command, Context


@command()
async def ping(context: Context):
    await context.send('pong')


def setup(bot):
    bot.add_command(ping)
