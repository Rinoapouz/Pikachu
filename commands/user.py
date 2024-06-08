import time
import disnake
from disnake.ext import commands


def commands_user(bot):

    @bot.command(name="commands")
    async def _commands(ctx) -> None:
        await ctx.reply("""```
    DOSY BOT COMMANDS
     
1. aricommands - shows you this menu
2. arifirst - shows you the first command that i created

ADMIN COMMANDS
3. ariclear [number] - Clear a certain number of messages
4. arinuke - Nukes the Channel
    
99. server_info - test
        ```""")

    @bot.command()
    async def first(ctx) -> None:
        await ctx.reply("works")
        await ctx.send("works2")


