from discord.errors import Forbidden
from discord.ext.commands import command, Context
from discord import User, Embed, Color, utils

@command()
async def mute(context: Context, user: User, *args):
    try:
        member = context.message.author
        role = utils.get(context.guild.roles, id=864593276735455262)
        await member.add_roles(role)
    except Forbidden:
        await context.send("Você não possui permissões para mutar um membro!")
    else:
        channel = context.bot.get_channel(id=862810594657959969)
        embed = Embed(title="Mute", color=Color.from_rgb(216, 42, 19))
        reason = ''
        
        if args:
            for arg in args:
                reason += ' ' + arg
        else:
            reason = "Ninguem mandou quebrar as regras, otário!"
        
        print(reason)
        embed.add_field(name=f"O usuário {user} foi mutado com sucesso.", value=f"{reason}")
        embed.set_footer(text=f"{context.message.author}", icon_url=context.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        
        await channel.send(embed=embed)

def setup(bot):
    bot.add_command(mute)
