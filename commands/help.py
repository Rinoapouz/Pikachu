import time
import disnake
from disnake.ext import commands

help = """```
        DOSY BOT COMMANDS

    1. aricommands - shows you this menu

    ADMIN COMMANDS
    3. ariclear [number] - Clear a certain number of messages
    4. arinuke - Nukes the Channel

    99. server_info - test
            ```"""


def hilfe(bot):
    @bot.slash_command(
        name="help",
        description="Show all commands")
    async def slashhelp(ctx) -> None:
        await ctx.send("""```
        DOSY BOT COMMANDS

    1. aricommands - shows you this menu

    ADMIN COMMANDS
    3. ariclear [number] - Clear a certain number of messages
    4. arinuke - Nukes the Channel

    99. server_info - test
            ```""")

    @bot.command(
        name="help")
    async def arihelp(ctx) -> None:
        await ctx.send("""```
            DOSY BOT COMMANDS

        1. aricommands - shows you this menu

        ADMIN COMMANDS
        3. ariclear [number] - Clear a certain number of messages
        4. arinuke - Nukes the Channel

        99. server_info - test
                ```""")
