from permissions.permissions import *


def ban(bot):
    @has_administrator_role()
    @bot.slash_command(
        name="ban",
        description="Ban a user")
    async def slashban(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        if member.id == ctx.author.id:
            await ctx.send("Du kannst dich nicht selbst bannen, tut mir leid! :)")
            return
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member} wurde für {reason} gebannt.")

    @has_administrator_role()
    @bot.command(
        name="ban",
        description="Ban a user",)
    async def ariban(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        if member.id == ctx.author.id:
            await ctx.send("Du kannst dich nicht selbst bannen, tut mir leid! :)")
            return
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member} wurde für {reason} gebannt.")
