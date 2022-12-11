import discord

def create_channel(ctx, *, channel_name):
    try:
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            return guild.create_text_channel(channel_name)
    except Exception as e:
        # Return error embed
        e_embed = discord.Embed(title="Error", description=f"{e}", color=0xff0000)
        return e_embed