import discord 
import asyncio
import os
import random
import datetime
from dotenv import load_dotenv

load_dotenv()

bot = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_member_join(member):
    if member == bot.user:
        return
    
    channel = discord.utils.get(member.guild.channels, name='general')
    response = f'Welcome to the server {member.mention}!'

    await channel.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    channel = message.channel
    response = f'Hello {message.author.mention}! Nano server is running!'
    await channel.send(response)

# @bot.event
# async def func():
    # channel =
    # response =  
    # await channel.send(response)
    
token = os.getenv('DISCORD_BOT_TOKEN')
bot.run(token)