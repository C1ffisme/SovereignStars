import os
from discord.ext import commands
from discord import client
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = client.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="ss!", intents=intents)


@bot.event
async def on_ready():
    print(bot.user.__repr__() + " has connected to Discord!")

    print("The bot is in the following guilds:")
    for guild in bot.guilds:
        print(guild.name)


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command()
async def square(ctx, arg):
    print(arg)
    await ctx.send(int(arg) ** 2)

bot.run(TOKEN)
