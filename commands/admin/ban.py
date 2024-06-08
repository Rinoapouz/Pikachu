import time
import disnake
from disnake.ext import commands
from permissions.administrator import *


def ban(bot):
    @bot.command()
    @has_administrator_role()
    async def ban(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        if member.id == ctx.author.id:
            await ctx.send("Du kannst dich nicht selbst bannen, tut mir leid! :)")
            return
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member} wurde für {reason} gebannt.")
