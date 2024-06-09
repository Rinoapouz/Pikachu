from permissions.permissions import *


def nuke(bot):
    @bot.command()
    @has_administrator_role()
    async def nuke(ctx) -> None:
        await ctx.channel.purge()
