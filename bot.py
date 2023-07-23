import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from functions import process_winners
from template import template

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
    # can access tuples with indexes, will use this to call functions to process each different command
    command = args[0]
    match command:
        case "winners":
            await process_winners(ctx, args)
        case "lb":
            await ctx.send(template)

    print("command: ", args[0])
    arguments = ", ".join(args)
    # await ctx.send(f'i read your command! i read {len(args)} args and they are: {arguments}')

# Run bot
bot.run(token=TOKEN)
