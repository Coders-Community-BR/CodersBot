from discord.errors import Forbidden
from discord.ext.commands import command, Context
from discord import User, Embed, Color

@command()
async def ban(context: Context, user: User, *args):
    try:
        await context.guild.ban(user)
    except Forbidden:
        await context.send('Você não possui permissões para banir um membro!')
    else:
        channel = context.bot.get_channel(id=862810594657959969)
        embed = Embed(title="Banimento", color=Color.dark_red())
        reason = ''
        
        if args:
            for arg in args:
                reason += ' ' + arg
        else:
            reason = "Ninguem mandou quebrar as regras, otário!"
        
        embed.add_field(name=f"O usuário {user} foi banido com sucesso.", value=f"{reason}")
        embed.set_footer(text=f"{context.message.author}", icon_url=context.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        
        await channel.send(embed=embed)
        
def setup(bot):
    bot.add_command(ban)
