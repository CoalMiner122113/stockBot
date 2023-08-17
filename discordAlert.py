import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
import yfinance as yf
import stockWatch

intents = discord.Intents.default()
# intents.members = True
# intents.presences = True
# intents.messages = True
# intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

#Necessary for .env file to work on py38
load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')

@bot.event
async def on_ready():
    print('Bot is ready.')
    await test_message_loop()

async def test_message_loop():
    
    while True:
        await asyncio.sleep(15)
        #get general channel
        channel = bot.get_channel(discord.utils.get(bot.get_all_channels(), name='general').id)
        response = (await stockWatch.current_price('BTC-USD'))
        await channel.send("BTC Price is: " + str(response))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #if 'btc' in message.content.lower():
    print("CompareMA called")
    for word in message.content.lower():
        print(word)
    channel = message.channel
    rating = (await stockWatch.compareMA('BTC-USD'))
    response = f'Hello {message.author.mention}! The current BTC rating is {rating}!'
    await channel.send(response)
    await bot.process_commands(message)


bot.run(bot_token)