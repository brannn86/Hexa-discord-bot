from discord.ext import commands
import discord
import random


TOKEN = "BOT_TOKEN"
CHANNEL_ID = 1059299802942287953 # default channel id


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command('help')


# initialize the bot

@bot.event
async def on_ready():
    print(f"{bot.user} is now running!") # bot status sent to terminal
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"{bot.user} is now running!") # bot status sent to specified channel


@bot.command()
async def help(ctx):
    await ctx.send(f"""Hello! This is Hexa. I'm currently in development
`!help` to show this message
`!roll` to roll a dice
`!add` add numbers in series
`!multiply` multiply numbers in series
`!divide` divide two numbers
`!translate` to be added
`!music` to be added
`!chatgpt` (implement ChatGPT) to be added
`!author` the creator""")
    return

@bot.command()
async def roll(ctx):
    await ctx.send(str(random.randint(1, 6)))
    return

@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(f"Result: {result}")

@bot.command()
async def multiply(ctx, *arr):
    result = 1
    for i in arr:
        result *= int(i)
    await ctx.send(f"Result: {result}")

@bot.command()
async def divide(ctx, x, y):
    result = int(x) / int(y)
    await ctx.send(f"Result: {result}")

@bot.command()
async def translate(ctx):
    await ctx.send("soon ;)")
    return

@bot.command()
async def author(ctx):
    await ctx.send("https://github.com/brannn86")
    return

bot.run(TOKEN)
