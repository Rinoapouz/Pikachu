import time
import disnake
from disnake.ext import commands
import sqlite3

database = sqlite3.connect('GoldenCat.sqlite')
cursor = database.cursor()


def level(bot):
    @bot.slash_command(
        name="level",
        description="Show your Level")
    async def slashlevel(ctx):

        rank = 1

        descending = "SELECT * FROM levels WHERE level = ? ORDER by exp DESC"
        cursor.execute(descending, (ctx.guild_id,))
        result = cursor.fetchall()

        for i in range(len(result)):

            if result[i][0] == ctx.guild.id:
                break
            else:
                rank += 1

        cursor.execute(
            f"SELECT exp, level, last_lvl FROM levels WHERE user_id = {ctx.author.id} AND guild_id = {ctx.guild.id}")
        result = cursor.fetchone()

        level = result[1]
        exp = result[0]
        last_lvl = result[2]

        next_lvl_xp = ((int(level) + 1) / 0.1) ** 2

        await ctx.send(f"You're level: {int(level)}")
