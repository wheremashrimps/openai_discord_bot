import io
import os
import datetime
import random
import openai
import discord
from discord.ext import commands
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from commands import davinci as d, bot_math as bm
from dotenv import load_dotenv
load_dotenv()

# TODO: Refactor commands into their own files in the commands folder

TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
API_KEY = os.getenv('API_KEY')
openai.api_key = API_KEY
openai.Model.retrieve(id="davinci")

davinci_txt = open("txt_files/davinci.txt", "a")
dalle_txt = open("txt_files/dalle.txt", "a")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
start_time = datetime.datetime.now()
BOT_TEMP = 0.5
MAX_TOKENS = 2000
TOP_P = 1
TOP_K = 0
FREQUENCY_PENALTY = 1.0
PRESENCE_PENALTY = 0.6

# Usage stats
dalle_uses = 0
davinci_uses = 0
total_uses = dalle_uses + davinci_uses


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@bot.command(name='create-channel', help='Creates a new text channel')
@commands.has_role('admin')
async def create_channel(ctx, *, channel_name):
    try:
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)
    except Exception as e:
        # Return error embed
        e_embed = discord.Embed(title="Error", description=f"{e}", color=0xff0000)
        await ctx.send(embed=e_embed)

@bot.command(name='delete-channel')
@commands.has_role('admin')
async def delete_channel(ctx, *, channel_name):
    try:
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if existing_channel:
            print(f'Deleting channel: {channel_name}')
            await existing_channel.delete()
    except Exception as e:
        # Return error embed
        e_embed = discord.Embed(title="Error", description=f"{e}", color=0xff0000)
        await ctx.send(embed=e_embed)

# If the user has the admin role, they can change the bot's settings
@bot.command(name='set', help='Changes the bot\'s settings')
@commands.has_role('admin')
async def set(ctx, setting, value):
    try:
        # Check if the setting exists
        if setting == "temp":
            global BOT_TEMP
            BOT_TEMP = float(value)
            await ctx.send(f"Set temperature to {value}")
        elif setting == "max_tokens":
            global MAX_TOKENS
            MAX_TOKENS = int(value)
            await ctx.send(f"Set max tokens to {value}")
        elif setting == "top_p":
            global TOP_P
            TOP_P = float(value)
            await ctx.send(f"Set top p to {value}")
        elif setting == "frequency_penalty":
            global FREQUENCY_PENALTY
            FREQUENCY_PENALTY = float(value)
            await ctx.send(f"Set frequency penalty to {value}")
        elif setting == "presence_penalty":
            global PRESENCE_PENALTY
            PRESENCE_PENALTY = float(value)
            await ctx.send(f"Set presence penalty to {value}")
        else:
            await ctx.send("That setting doesn't exist")
    except Exception as e:
        # Return error embed
        e_embed = discord.Embed(title="Error", description=f"{e}", color=0xff0000)
        total_uses += 1
        await ctx.send(embed=e_embed)

# Create a command to display the bot's stats
@bot.command(name='stats', help='Displays the bot\'s stats')
async def stats(ctx):
    try:
        
        # Get the time the bot has been running
        current_time = datetime.datetime.now()
        time_running = current_time - start_time
        # Get the number of commands used
        total_uses = dalle_uses + davinci_uses
        # Create the embed
        embed = discord.Embed(title="Bot Stats", description="Here are the bot's current stats", color=0xeee657)
        embed.add_field(name="Time Running", value=time_running, inline=False)
        embed.add_field(name="Total Uses", value=total_uses, inline=False)
        embed.add_field(name="Davinci Uses", value=davinci_uses, inline=False)
        embed.add_field(name="DALLE Uses", value=dalle_uses, inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        # Send error embed
        embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xe74c3c)
        total_uses += 1
        await ctx.send(embed=embed)


# Create a command to display the bot's settings embed
@bot.command(name='settings', help='Displays the bot\'s settings')
async def settings(ctx):
    try:
        embed = discord.Embed(title="Bot Settings", description="Here are the bot's current settings", color=0xeee657)
        embed.add_field(name="Temperature", value=BOT_TEMP, inline=False)
        embed.add_field(name="Max Tokens", value=MAX_TOKENS, inline=False)
        embed.add_field(name="Top P", value=TOP_P, inline=False)
        embed.add_field(name="Frequency Penalty", value=FREQUENCY_PENALTY, inline=False)
        embed.add_field(name="Presence Penalty", value=PRESENCE_PENALTY, inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        # Send error embed
        embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xe74c3c)
        total_uses += 1
        await ctx.send(embed=embed)

###############################################################################

# Create a command embed to display the bot's commands
@bot.command(name='commands', help='Displays the bot\'s commands')
async def commands(ctx):
    embed = discord.Embed(title="Commands", description="Here are the commands you can use:", color=0xeee657)
    embed.add_field(name="!dalle", value="Generates images using DALL-E\nEnd your prompt with an integer between 1-10 to generate multiple images", inline=False)
    embed.add_field(name="!davinci", value="Generates text using Davinci", inline=False)
    embed.add_field(name="!gpt3", value="Generates text using GPT-3", inline=False)
    embed.add_field(name="!math", value="Solves math problems", inline=False)
    embed.add_field(name="!convert", value="Convert a unit from one to another", inline=False)
    embed.add_field(name="!settings", value="Displays the bot's settings", inline=False)
    embed.add_field(name="!commands", value="Displays the bot's commands", inline=False)
    total_uses += 1
    await ctx.send(embed=embed)


# A message embed for the DALLE command
@bot.command(name='dalle', help='Generates images using DALL-E')
async def dalle(ctx, *, prompt):
    # Write the prompt and the corresponding image url to a file
    dalle_txt.write(f"{prompt} - ")
    # Create a list to store the urls
    urls = []
    # Get the number of images to generate from the end of the prompt
    num_images = int(prompt[-1])
    # Remove the number from the prompt
    prompt = prompt[:-1]
    # Iterate through the number of images to generate
    for i in range(num_images):
        # Generate an image
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        # Get the image url
        image_url = response['data'][0]['url']
        # Add the image url to the list
        urls.append(image_url)
        # Write the image url to the file
        dalle_txt.write(f"{image_url} - ")
    # Write a new line to the file
    dalle_txt.write("\n")

    # Iterate through the list of urls
    for url in urls:
        # Create an embed with the image url
        embed = discord.Embed(title="DALL-E", description=prompt.title(), color=0xeee657)
        embed.set_image(url=url)
        # Send the embed
        await ctx.send(embed=embed)
    dalle_uses += 1

# A bot command that generates text using Davinci and sends it as a prompt to the dalle bot command as input
@bot.command(name='gm', help='Generates text using Davinci and sends it as a prompt to the dalle bot command as input')
async def god_mode(ctx, *, prompt):
    davinci_prompt = prompt.title()
    embed = discord.Embed(title=davinci_prompt, description=f'Davinci Response: {d.return_response(davinci_prompt)}', color=0xeee657)
    # Remove the number from the prompt
    image = openai.Image.create(
        prompt=d.return_response(prompt),
        n=1,
        size="1024x1024"
    )
    image_url = image['data'][0]['url']
    embed.set_image(url=image_url)
    davinci_uses += 1
    dalle_uses += 1
    await ctx.send(embed=embed)



# Create a function that creates a dictionary of urls and their corresponding prompts from the urls.txt file
def create_dict():
    # Create a dictionary to store the urls and their corresponding prompts
    url_dict = {}
    # Open the urls.txt file
    f = open("txt_files/urls.txt", "r")
    # Read the file
    data = f.read()
    # Split the file into a list
    data = data.split('\n')
    # Iterate through the list
    for line in data:
        # If the line is a url
        if line.startswith('URL:'):
            # Get the url
            url = line[4:]
            # Get the prompt
            prompt = data[data.index(line) - 1][7:]
            # Add the url and the prompt to the dictionary
            url_dict[url] = prompt
    # Return the dictionary
    return url_dict

# Create a command to create an embed with a random image and its prompt using the create_dict() function
@bot.command(name='random-image', help='Displays a random image and its corresponding prompt')
async def random_image(ctx):
    # Create a dictionary of urls and their corresponding prompts
    url_dict = create_dict()
    # Get a random url from the dictionary
    url = random.choice(list(url_dict.keys()))
    # Create an embed with the image url and its prompt
    embed = discord.Embed(title="DALL-E", description=url_dict[url].title(), color=0xeee657)
    embed.set_image(url=url)
    total_uses += 1
    # Send the embed
    await ctx.send(embed=embed)

# Create a command to generate text using Davinci and display it in an embed
# and save the prompt and the response to a file (davinci.txt)
@bot.command(name='davinci', help='Generates text using Davinci')
async def davinci(ctx, *, prompt):
        # Create a dictionary to store the responses and their corresponding prompts
        response_dict = {}
        # Open the davinci.txt file
        f = open("txt_files/davinci.txt", "r")
        # Read the file
        data = f.read()
        # Split the file into a list
        data = data.split('\n')
        # Iterate through the list
        for line in data:
            # If the line is a response
            if line.startswith('RESPONSE:'):
                # Get the response
                response = line[9:]
                # Get the prompt
                prompt = data[data.index(line) - 1][7:]
                # Add the response and the prompt to the dictionary
                response_dict[response] = prompt
        # Create a list to store the responses
        responses = []
        # Iterate through the dictionary
        for response in response_dict:
            # If the prompt is in the dictionary
            if prompt in response_dict[response]:
                # Add the response to the list
                responses.append(response)
        # If the prompt is not in the dictionary
        if prompt not in response_dict.values():
            # Generate a response
            response = d.gpt_response(prompt)
            # Add the response to the list
            responses.append(response)
            # Write the prompt and the response to the file
            davinci_txt.write(f"PROMPT: {prompt}\nRESPONSE: {response}\n\n")
        # Get a random response from the list
        response = random.choice(responses)
        # Create an embed with the response
        embed = discord.Embed(
            title = 'Davinci Response',
            description = response,
            colour = discord.Colour.blue()
        )
        davinci_uses += 1
        # Send the embed
        await ctx.send(embed=embed)
        # Close the file
        f.close()
        

def create_davinci_dict():
    # Create a dictionary to store the responses and their corresponding prompts
    response_dict = {}
    # Open the davinci.txt file
    f = open("txt_files/davinci.txt", "r")
    # Read the file
    data = f.read()
    # Split the file into a list
    data = data.split('\n')
    # Iterate through the list
    for line in data:
        # If the line is a response
        if line.startswith('RESPONSE:'):
            # Get the response
            response = line[9:]
            # Get the prompt
            prompt = data[data.index(line) - 1][7:]
            # Add the response and the prompt to the dictionary
            response_dict[response] = prompt
    # Return the dictionary
    return response_dict

# Create a command to create an embed with a random response and its prompt using the create_davinci_dict() function
@bot.command(name='random-response', help='Displays a random response and its corresponding prompt')
async def random_response(ctx):
    # Create the dictionary
    response_dict = create_davinci_dict()
    # Get a random response
    response = random.choice(list(response_dict.keys()))
    # Create the embed
    embed = discord.Embed(
        title = 'Random Davinci Response',
        description = response,
        colour = discord.Colour.blue()
    )
    total_uses += 1
    # Send the embed
    await ctx.send(embed=embed)

###############################################################################

# A command to display the bot's latency
@bot.command(name='ping', help='Displays the bot\'s latency')
async def ping(ctx):
    # Create the embed
    embed = discord.Embed(
        title = 'Ping',
        description = f'Pong :pong: {round(bot.latency * 1000)}ms',
        colour = discord.Colour.blue()
    )
    total_uses += 1
    # Send the embed
    await ctx.send(embed=embed)

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
    total_uses += 1
    # Send the embed
    await ctx.send(embed=embed)

# Display the bots uses
@bot.command(name='uses', help='Displays the bot\'s uses')
async def uses(ctx):
    # Create the embed
    embed = discord.Embed(
        title = 'Uses',
        description = f'DALL-E uses: {dalle_uses}\nDavinci uses: {davinci_uses}',
        colour = discord.Colour.blue()
    )
    total_uses += 1
    # Send the embed
    await ctx.send(embed=embed)


###############################################################################

#A command that takes an x and y coordinate and displays a graph of the function f(x) = x^2 + y^2 using matplotlib
@bot.command(name='graph', help='Displays a graph of the function f(x) = x^2 + y^2')
async def graph(ctx, x: int, y: int):
    # Create figure object and plot function and set axis labels and title, and create a line that displays the function
    fig = plt.figure()
    plt.plot(x, x**2 + y**2, 'ro')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Graph of f({x}) = {x}^2 + {y}^2')

    # Save figure to buffer and create file object
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    file = discord.File(buf, filename='graph.png')

    # Create embed with image and send it
    embed = discord.Embed()
    # Set the title
    embed.title = f'Graph of f({x}) = {x}^2 + {y}^2'
    embed.set_image(url='attachment://graph.png')
    await ctx.send(file=file, embed=embed)

# A command that takes a number and displays a graph of the function f(x) = x^2 using matplotlib
@bot.command(name='graph2', help='Displays a graph of the function f(x) = x^2')
async def graph2(ctx, x: int):
    # Create figure object and plot function and set axis labels and title, and create a line that displays the function
    fig = plt.figure()
    plt.plot(x, x**2, 'ro')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Graph of f({x}) = {x}^2')

    # Save figure to buffer and create file object
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    file = discord.File(buf, filename='graph.png')

    # Create embed with image and send it
    embed = discord.Embed()
    # Set the title
    embed.title = f'Graph of f({x}) = {x}^2'
    embed.set_image(url='attachment://graph.png')
    await ctx.send(file=file, embed=embed)

# A graph that shows a y = mx + b graph
@bot.command(name='graph3', help='Displays a graph of the function f(x) = mx + b')
async def graph3(ctx, m: int, b: int, x: int):
    # Create figure object and plot function and set axis labels and title, and create a line that displays the function
    fig = plt.figure()
    plt.plot(m, m * x + b, 'ro')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Graph of f({m}) = {m}x + {b}')

    # Save figure to buffer and create file object
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    file = discord.File(buf, filename='graph.png')

    # Create embed with image and send it
    embed = discord.Embed()
    # Set the title
    embed.title = f'Graph of f({m}) = {m}x + {b}'
    embed.set_image(url='attachment://graph.png')
    await ctx.send(file=file, embed=embed)

# A command that will perform basic math operations
@bot.command(name='math', help='Performs basic math operations')
async def math(ctx, x: int, operator: str, y: int):
    embed = discord.Embed(
        title = f'{x} {operator} {y}',
        description=f'{bm.bot_math(x, operator, y)}',
        colour = discord.Colour.blue()
    )
    await ctx.send(embed=embed)

    

# A command that will convert a number from one unit to another
@bot.command(name='convert', help='Converts a number from one unit to another')
async def convert(ctx, number: float, unit1: str, unit2: str):
    from commands import convert as c
    c.convert(number, unit1, unit2)
    
################################################################################




bot.run(TOKEN)
