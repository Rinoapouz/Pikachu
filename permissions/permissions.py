import time
import disnake
from disnake.ext import commands

# Definieren Sie eine Liste von Rollennamen oder IDs, die die Befehle verwenden dürfen
administrator_role = ['Admin', 'Moderator']  # Ersetzen Sie dies durch Ihre Rollennamen oder IDs


def has_administrator_role():
    async def predicate(ctx):
        # Überprüfen, ob der Benutzer eine der zulässigen Rollen hat
        return any(
            role.name in administrator_role for role in ctx.author.roles) or ctx.author.guild_permissions.administrator

    return commands.check(predicate)
