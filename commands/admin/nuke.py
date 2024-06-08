import time
import disnake
from disnake.ext import commands
from permissions.administrator import *


def nuke(bot):
    @bot.command()
    @has_administrator_role()
    async def nuke(ctx) -> None:
        await ctx.channel.purge()
