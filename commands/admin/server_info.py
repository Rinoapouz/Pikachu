import time
import disnake
from disnake.ext import commands
from permissions.administrator import *


def server_info(bot):
    # Guck in CMD, Lösche ich später
    @bot.command()
    @has_administrator_role()
    async def server_info(ctx):
        for guild in bot.guilds:
            print(
                f"[Server Name: {guild.name}] [ID: {guild.id}] | Server Owner: [{guild.owner}]")  # prints all server's names
