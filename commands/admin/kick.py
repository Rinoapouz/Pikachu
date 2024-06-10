from permissions.permissions import *
import disnake
from disnake.ext import commands


def kick(bot):
    @has_administrator_role()
    @bot.slash_command(
        name="kick",
        description="Kick a user")
    async def slashkick(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        await member.kick(reason=reason)
        await ctx.send(f"{member} wurde für {reason} gekickt.")

    @has_administrator_role()
    @bot.command(
        name="kick",
        description="Kick a user")
    async def arikick(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        await member.kick(reason=reason)
        await ctx.send(f"{member} wurde für {reason} gekickt.")
