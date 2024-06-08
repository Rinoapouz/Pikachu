import time
import disnake
from disnake.ext import commands
from permissions.administrator import *


def clear(bot):
    @bot.command()
    @has_administrator_role()
    async def clear(ctx, message: int) -> None:
        await ctx.channel.purge(limit=message + 1)  # message + 1, um die Befehlsnachricht selbst einzuschließen
