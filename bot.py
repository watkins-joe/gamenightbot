import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load token from env variable
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Initialize intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game('testing')
    )
    print('Bot is ready.')


# When !gn command is entered
@bot.command(name="gn")
async def on_gn(ctx, *args):
    arguments = ", ".join(args)
    await ctx.send(f'i read your command. args: {arguments}')

# Run bot
bot.run(token=TOKEN)
