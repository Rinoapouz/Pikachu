# Import für USER Commands
from commands.help import *
from commands.level import *
# Import für ADMIN Commands
from commands.admin.ban import *
from commands.admin.clear import *
from commands.admin.kick import *
from commands.admin.nuke import *
# Import von Addons
from addons.Levelsystem.levelsystem import *


# Liste der commands
admin_commands = [ban, clear, kick, nuke]
user_commands = [hilfe, level]
# Liste der Addons
addons = [Leveling]


# Bot Einstellungen
bot = commands.Bot(
    command_prefix="ari",
    intents=disnake.Intents.all(),
    help_command=None,
    activity=disnake.Game(name="/help")
)

@bot.event
async def on_ready():
    print(f"Der Bot ist nun an! | username = {bot.user}")

# Commands registrieren
for command in user_commands:
    command(bot)
for command in admin_commands:
    command(bot)
for command in addons:
    command(bot)

bot.run("MTE3NTAwNTgyODc5Nzk2ODQwNQ.GTXkVh.34N-dTa3pbTzZd__qStYTYHhPvPZ7xJQNBQpy8")
