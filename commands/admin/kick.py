import time
import disnake
from disnake.ext import commands
from permissions.administrator import *


def kick(bot):
    @bot.command()
    @has_administrator_role()
    async def kick(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        await member.kick(reason=reason)
        await ctx.send(f"{member} wurde für {reason} gekickt.")
