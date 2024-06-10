from permissions.permissions import *
import disnake
from disnake.ext import commands


def nuke(bot):
    @has_administrator_role()
    @bot.slash_command(
        name="nuke",
        description="Clear the channel")
    async def slashnuke(ctx) -> None:
        await ctx.channel.purge()

    @has_administrator_role()
    @bot.command(
        name="nuke",
        description="Clear the channel")

    async def arinuke(ctx) -> None:
        await ctx.channel.purge()
