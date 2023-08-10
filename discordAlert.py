import discord 
import asyncio
import os
import random
import datetime

bot = discord.Client()

@bot.event
async def on_member_join(member):
    if member == bot.user:
        return
    
    channel = discord.utils.get(member.guild.channels, name='general')
    response = f'Welcome to the server {member.mention}!'

    await channel.send(response)

@bot.event
async def on_message(message):
    if message.author = bot.user:
        return
    
    channel = message.channel
    response = f'Hello {message.author.mention}! Nano server is running!'
    await channel.send(response)

# @bot.event
# async def crypto_reminder():
    # await
# 