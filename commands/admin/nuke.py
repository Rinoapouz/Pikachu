import time

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
        embed = disnake.Embed(
            title=f"The channel has been nuked.",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed)

    @has_administrator_role()
    @bot.command(
        name="nuke",
        description="Clear the channel")
    async def arinuke(ctx) -> None:
        await ctx.channel.purge()

        embed = disnake.Embed(
            title=f"The channel has been nuked.",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed)
