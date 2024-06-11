import time
import disnake
from disnake.ext import commands

# Import von USER Commands
from commands.help import *
# Import von ADMIN Commands
from commands.admin.ban import *
from commands.admin.clear import *
from commands.admin.kick import *
from commands.admin.nuke import *
from commands.admin.server_info import *

# Liste der commands
admin_commands = [ban, clear, kick, nuke, server_info]
client_commands = [hilfe]

# Prefix bestimmen = ari, disnake help commands deaktiviert
bot = commands.Bot(
    command_prefix="ari",
    intents=disnake.Intents.all(),
    help_command=None
)


@bot.event
async def on_ready():
    print(f"Bot is running | {bot.user}")


# Commands registrieren
for command in client_commands:
    command(bot)
for command in admin_commands:
    command(bot)

bot.run("MTE3NTAwNTgyODc5Nzk2ODQwNQ.GTXkVh.34N-dTa3pbTzZd__qStYTYHhPvPZ7xJQNBQpy8")
