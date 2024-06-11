import time
import disnake
from disnake.ext import commands


def hilfe(bot):
    @bot.slash_command(
        name="help",
        description="Show all commands")
    async def slashhelp(ctx) -> None:
        embed = disnake.Embed(
            title="HERE ARE ALL THE COMMANDS",
            description="The Golden Cat uses **ari** as a command prefix. **slash** will also work",
            color=disnake.Color.yellow()
        )

        embed.add_field(
            name="Default",
            value="""```
/help

                ```""",
            inline=True
        )

        embed.add_field(
            name="information",
            value="""```
soon...
                ```""",
            inline=True
        )

        embed.add_field(
            name="Administrator",
            value="""```
/ban
/kick
/clear
/nuke
                ```""",
            inline=True
        )

        await ctx.send(embed=embed)

    @bot.command(
        name="help")
    async def arihelp(ctx) -> None:
        embed = disnake.Embed(
            title="HERE ARE ALL THE COMMANDS",
            description="The Golden Cat uses **ari** as a command prefix. **slash** will also work",
            color=disnake.Color.yellow()
        )

        embed.add_field(
            name="Default",
            value="""```
/help

                ```""",
            inline=True
        )

        embed.add_field(
            name="information",
            value="""```
soon...
                ```""",
            inline=True
        )

        embed.add_field(
            name="Administrator",
            value="""```
/ban
/kick
/clear
/nuke
                ```""",
            inline=True
        )

        await ctx.send(embed=embed)
