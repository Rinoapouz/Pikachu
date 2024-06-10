from permissions.permissions import *
import disnake
from disnake.ext import commands


def clear(bot):
    @has_administrator_role()
    @bot.slash_command(
        name='clear',
        description='Clear a sort of content')
    async def slashclear(ctx, message: int) -> None:
        await ctx.channel.purge(limit=message + 1)  # message + 1, um die Befehlsnachricht selbst einzuschließen

    @has_administrator_role()
    @bot.command(
        name='clear',
        description='Clear a sort of content')
    async def ariclear(ctx, message: int) -> None:
        await ctx.channel.purge(limit=message + 1)  # message + 1, um die Befehlsnachricht selbst einzuschließen
