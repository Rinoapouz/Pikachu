import time
import disnake
from disnake.ext import commands

from commands.help import *

from commands.admin.ban import *
from commands.admin.clear import *
from commands.admin.kick import *
from commands.admin.nuke import *
from commands.admin.server_info import *

# Liste der erlaubten Server-IDs
allowed_server_ids = [1248558780195799041, 808816437363343380]

# Liste der commands
admin_commands = [ban, clear, kick, nuke, server_info]
client_commands = [hilfe]


# Prefix wurde bestimmt (Standard /)
bot = commands.Bot(
    command_prefix="ari",
    intents=disnake.Intents.all(),
    help_command=None
)


# Überprüfe die Server-IDs und leavt unerwünschte Server
@bot.event
async def on_ready():
    print(f"Bot is running | {bot.user}")
    # Überprüfe die Server-IDs und leavt unerwünschte Server
    for guild in bot.guilds:
        if guild.id not in allowed_server_ids:
            await guild.leave()
            print(f"Left server [{guild.name}] [ID: {guild.id}] | Server Owner: [{guild.owner}]")


# Überprüft, ob der Bot einem unbekannten Server beitritt, wenn ja = verlassen
@bot.event
async def on_guild_join(guild):
    if guild.id not in allowed_server_ids:
        await guild.leave()
        print(f"Left server [{guild.name}] [ID: {guild.id}] | Server Owner: [{guild.owner}]")


# Registrier commands
for command in client_commands:
    command(bot)

for command in admin_commands:
    command(bot)


bot.run("MTE3NTAwNTgyODc5Nzk2ODQwNQ.GTXkVh.34N-dTa3pbTzZd__qStYTYHhPvPZ7xJQNBQpy8")
