from permissions.permissions import *
import disnake
from disnake.ext import commands


def kick(bot):
    @has_administrator_role()
    @bot.slash_command(
        name="kick",
        description="Kick a user",
        options=[
            disnake.Option(
                name="member",
                description="The member to kick",
                type=disnake.OptionType.user,
                required=True
            ),
            disnake.Option(
                name="reason",
                description="The reason for the kick",
                type=disnake.OptionType.string,
                required=False,
            )
        ]
    )
    async def slashkick(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        await member.kick(reason=reason)

        embed = disnake.Embed(
            title=f"{ctx.author.name} kicked a user",
            color=disnake.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url)

        embed.add_field(name="User", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        await ctx.send(embed=embed)

    @has_administrator_role()
    @bot.command(
        name="kick",
        description="Kick a user",
        options=[
            disnake.Option(
                name="member",
                description="The member to kick",
                type=disnake.OptionType.user,
                required=True
            ),
            disnake.Option(
                name="reason",
                description="The reason for the kick",
                type=disnake.OptionType.string,
                required=False,
            )
        ]
    )
    async def slashkick(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        await member.kick(reason=reason)

        embed = disnake.Embed(
            title=f"{ctx.author.name} kicked a user",
            color=disnake.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url)

        embed.add_field(name="User", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        await ctx.send(embed=embed)