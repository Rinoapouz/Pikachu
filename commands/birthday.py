import time
import disnake
from disnake.ext import commands
import sqlite3

database = sqlite3.connect('GoldenCat.sqlite')
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Birthday(user_id INTERGER, day INTEGER, mounth INTEGER)""")


def birthday(bot):
    @bot.slash_command(
        name="birthday",
        description="Set ur Birthday",
        options=[
            disnake.Option(
                name="day",
                description="The day of your Birthday",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="mounth",
                description="The mounth of your Birthday",
                type=disnake.OptionType.string,
                required=True,
            )
        ]
    )
    async def slashbirthday(ctx, day, mounth) -> None:
        
        cursor.execute(f"SELECT user_id, day, mounth FROM birthday WHERE user_id = {ctx.author.id}")
        results = cursor.fetchone()

        if results == None:
            
            cursor.execute(f"INSERT INTO birthday(user_id, day, mounth) VALUES({ctx.author.id}, )")
            database.commit()

        await ctx.send("Birthday setted")