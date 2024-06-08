import time
import disnake
from disnake.ext import commands


def help(bot):
    @bot.command(name="help")
    async def help(ctx) -> None:
        await ctx.reply("""```
        DOSY BOT COMMANDS

    1. aricommands - shows you this menu

    ADMIN COMMANDS
    3. ariclear [number] - Clear a certain number of messages
    4. arinuke - Nukes the Channel

    99. server_info - test
            ```""")
