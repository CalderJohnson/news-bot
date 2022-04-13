"""news bot"""

#config

prefix = '!'
token = 'your-token'

#imports

import datetime
from datagatherer import format_news, get_news_data
import discord
from discord.ext import commands
import json

#initialization

client = commands.Bot(command_prefix=prefix)

#events

@client.event
async def on_ready():
    """triggers when bot is running"""
    activity = discord.Game(name="Informing the people", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot online")

@client.event
async def on_guild_join(server):
    """triggers on server join"""
    print("Joining {0}".format(server.name))

#cmds

@client.command(pass_context=True)
async def news(ctx):
    """post news to channel"""
    with open('newsdata.json', 'r') as newsdata:
        get_news_data()
        newsfile = json.load(newsdata)
        articles = len(newsfile["articles"])
        channel = client.get_channel(873760273964625980)
        today = str(datetime.date.today())
        await channel.send("**__News of " + today + "__**")
        for i in range(articles):
            await channel.send(embed=(format_news((newsfile["articles"])[i])))
            
client.run(token)
