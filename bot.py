#imports
import os
import discord
from dotenv import load_dotenv, find_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        
    print(
        f"{client.user} has connected to discord\n"
        f"{guild.name}, id: {guild.id}\n"
    )

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Members:\n - {members}")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"lmao, {member} is such a dumb name lol"
    )

client.run(TOKEN)
