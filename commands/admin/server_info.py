from permissions.permissions import *


def server_info(bot):
    # Guck in CMD, Lösche ich später
    @bot.command()
    @has_administrator_role()
    async def ariserver_info(ctx):
        for guild in bot.guilds:
            print(
                f"[Server Name: {guild.name}] [ID: {guild.id}] | Server Owner: [{guild.owner}]")  # prints all server's names