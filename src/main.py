# Import extern Libarys
import os
from dotenv import load_dotenv, find_dotenv

# Import all user commands
from commands.help import *
from commands.level import *
# Import all admin commands
from commands.admin.ban import *
from commands.admin.clear import *
from commands.admin.kick import *
from commands.admin.nuke import *
# Import Addons
from addons.Levelsystem.levelsystem import *

# Liste der commands
admin_commands = [ban, clear, kick, nuke]
user_commands = [hilfe, level]
# Liste der Addons
addons = [Leveling]

# Bot Settings
bot = commands.Bot(
    command_prefix="ari",
    intents=disnake.Intents.all(),
    help_command=None,
    activity=disnake.Game(name="/help")
)

# When the Bot is ready it should say "Bot working on = Botusername"
@bot.event
async def on_ready():
    print(f"Bot working on = {bot.user}")


# Register all commands
for command in user_commands:
    command(bot)
for command in admin_commands:
    command(bot)
for command in addons:
    command(bot)


# Find and load the .env file with the Discord Token
dotenv_path = find_dotenv('Zoken.env')
print(f".env file found: {dotenv_path}")
load_dotenv(dotenv_path)

# load the Discord Bot Token Start the bot
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
