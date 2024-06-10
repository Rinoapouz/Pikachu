from permissions.permissions import *
import disnake
from disnake.ext import commands


def ban(bot):
    @has_administrator_role()
    @bot.slash_command(
        name="ban",
        description="Ban a user",
        options=[
            disnake.Option(
                name="member",
                description="The member to ban",
                type=disnake.OptionType.user,
                required=True
            ),
            disnake.Option(
                name="reason",
                description="The reason for the ban",
                type=disnake.OptionType.string,
                required=False,
            )
        ]
    )
    async def slashban(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        if member.id == ctx.author.id:
            await ctx.send("You can't ban yourself, idiot! :)")
            return
        await ctx.guild.ban(member, reason=reason)

        embed = disnake.Embed(
            title="The banhammer slained a user",
            color=disnake.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url)

        embed.add_field(name="User", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.add_field(name="Length", value=f"permanent", inline=True)
        await ctx.send(embed=embed)

    @has_administrator_role()
    @bot.command(
        name="ban",
        description="Ban a user",
        options=[
            disnake.Option(
                name="member",
                description="The member to ban",
                type=disnake.OptionType.user,
                required=True
            ),
            disnake.Option(
                name="reason",
                description="The reason for the ban",
                type=disnake.OptionType.string,
                required=False,
            )
        ]
    )
    async def ariban(ctx, member: disnake.Member, *, reason: str = "Kein Grund angegeben") -> None:
        if member.id == ctx.author.id:
            await ctx.send("You can't ban yourself, idiot! :)")
            return
        await ctx.guild.ban(member, reason=reason)

        embed = disnake.Embed(
            title="The banhammer slained a user",
            color=disnake.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url)

        embed.add_field(name="User", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.add_field(name="Length", value=f"permanent", inline=True)
        await ctx.send(embed=embed)
