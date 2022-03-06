import discord
from discord.ext import commands
import os
from discord.ext.commands import CommandNotFound
from replit import db

client = commands.Bot(command_prefix='!')
count = db["number"]

@client.event
async def on_ready():
    print('Bot online and ready to count. Count: ' + str(count))

@client.event
async def on_message(message):
    if message.author.id == 280121868533628929:
        if ':KEKW:' in message.content:
          count = db["number"]
          x = int(count) + 1
          db["number"] = str(x)
          await message.channel.send('AK has used kekw ' + str(x) + ' times.')

@client.event
async def on_message(message):
    if message.author.id == 280121868533628929:
        if ':kekw:' in message.content:
          count = db["number"]
          x = int(count) + 1
          db["number"] = str(x)
          await message.channel.send('AK has used kekw ' + str(x) + ' times.')

client.run(os.environ['TOKEN'])
