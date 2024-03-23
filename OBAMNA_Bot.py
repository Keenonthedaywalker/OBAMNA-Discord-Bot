# This example requires the 'message_content' intent.

import discord
import discord.client
import os 
import requests
import time
import asyncio
from discord import Intents, Client, Message
from discord.ext import tasks
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot


# Intents are permissions that the bot need in order to do things.
intents = discord.Intents.default()
intents.message_content = True

#client = MyClient(intents=intents)
client = discord.Client(intents=intents)

@tasks.loop(minutes=3)
async def test():
    channel = client.get_channel("Text channel code goes here to send messages in. Remove these quotes.")
    await channel.send("OBAMNA")

@tasks.loop(minutes=3)
async def sound_test():
    channel = client.get_channel("Voice channel code goes here to play sound in. Remove these quotes. ")
    voice = await channel.connect()
    source = FFmpegPCMAudio('OBAMNA.mp4')
    player = voice.play(source)
    await asyncio.sleep(5)
    await voice.disconnect()


@client.event
async def on_ready():
        print(f'Logged on as {client.user}!')
        test.start()
        sound_test.start()
        check.start()

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

#Super secret auth code goes here, in quotes.
client.run('')