import time
import disnake
from disnake.ext import commands

administrator_role = ['Admin', 'Moderator']  # Ersetzen Name oder IDs


# Überprüfen, ob der Benutzer einer der zulässigen Rollen hat
def has_administrator_role():
    async def predicate(ctx):
        return any(
            role.name in administrator_role for role in ctx.author.roles) or ctx.author.guild_permissions.administrator

    return commands.check(predicate)
