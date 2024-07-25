import time
import disnake
from disnake.ext import commands
import sqlite3

database = sqlite3.connect('GoldenCat.sqlite')
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Birthday(user_id INTERGER, guild_id INTEGER, day INTEGER, mouth INTEGER, year INTEGER)""")


def birthday(bot):
    @bot.event
    async def on_message(ctx):
        print("hello world")