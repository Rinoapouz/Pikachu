import time
import disnake
from disnake.ext import commands

# Definieren Sie eine Liste von Rollennamen oder IDs, die die Befehle verwenden dürfen
ALLOWED_ROLES = ['Admin', 'Moderator']  # Ersetzen Sie dies durch Ihre Rollennamen oder IDs


def has_allowed_role():
    async def predicate(ctx):
        # Überprüfen, ob der Benutzer eine der zulässigen Rollen hat
        return any(
            role.name in ALLOWED_ROLES for role in ctx.author.roles) or ctx.author.guild_permissions.administrator

    return commands.check(predicate)


def commands_admin(bot):
    @bot.command()
    @has_allowed_role()
    async def clear(ctx, message: int) -> None:
        await ctx.channel.purge(limit=message + 1)  # message + 1, um die Befehlsnachricht selbst einzuschließen

    @bot.command()
    @has_allowed_role()
    async def nuke(ctx) -> None:
        await ctx.channel.purge()

    @bot.command()
    @has_allowed_role()
    async def kick(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        await member.kick(reason=reason)
        await ctx.send(f"{member} wurde für {reason} gekickt.")

    @bot.command()
    @has_allowed_role()
    async def ban(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        if member.id == ctx.author.id:
            await ctx.send("Du kannst dich nicht selbst bannen, tut mir leid! :)")
            return
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member} wurde für {reason} gebannt.")

    # Guck in CMD, Lösche ich später
    @bot.command()
    @has_allowed_role()
    async def server_info(ctx):
        for guild in bot.guilds:
            print(f"[Server Name: {guild.name}] [ID: {guild.id}] | Server Owner: [{guild.owner}]")  # prints all server's names