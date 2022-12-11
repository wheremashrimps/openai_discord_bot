from discord.ext import commands
import discord
import datetime

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Get the time the bot was started
start_time = datetime.datetime.now()

# A command to display the bot's uptime
@bot.command(name='uptime', help='Displays the bot\'s uptime')
async def uptime(ctx):
    # Get the current time
    now = datetime.datetime.now()
    # Get the difference between the current time and the time the bot was started
    delta = now - start_time
    # Create the embed
    embed = discord.Embed(
        title = 'Uptime',
        description = f'{delta}',
        colour = discord.Colour.blue()
    )
    # Send the embed
    await ctx.send(embed=embed)
