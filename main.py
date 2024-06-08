import disnake
from disnake.ext import commands
from commands.commands_user import commands_user
from commands.commands_admin import commands_admin

# Liste der erlaubten Server-IDs
allowed_server_ids = [1248558780195799041, 808816437363343380]

# Prefix wurde bestimmt (Standard /)
bot = commands.Bot(
    command_prefix="ari",
    intents=disnake.Intents.all()
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
    if guild.id not in allowed_server_ids:
        await guild.leave()
        print(f"Left server [{guild.name}] [ID: {guild.id}] | Server Owner: [{guild.owner}]")


# Importiere und registriere die Kommandos
commands_admin(bot)
commands_user(bot)

bot.run("MTE3NTAwNTgyODc5Nzk2ODQwNQ.GTXkVh.34N-dTa3pbTzZd__qStYTYHhPvPZ7xJQNBQpy8")
