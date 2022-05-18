"""news bot"""
#imports

import datetime
import json
import discord
from discord.ext.commands import Bot
from datagatherer import format_news, get_news_data
from keys import BOT_TOKEN

#config

PREFIX = '!'
TOKEN = BOT_TOKEN

#initialization

client = Bot(command_prefix=PREFIX)

#events

@client.event
async def on_ready():
    """triggers when bot is running"""
    activity = discord.Game(name="Informing the people", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot online")

@client.event
async def on_guild_join(guild):
    """Triggers on server join"""
    print(f'Joining {guild.name}')
    await guild.create_text_channel("news")
    channel = discord.utils.get(guild.channels, name="news")
    await channel.send("Channel set!")
    with open('serverdata.json', 'a', encoding='utf-8') as serverdata:
        json.dump(channel.id, serverdata)

#cmds

@client.command(pass_context=True)
async def news(ctx):
    """Post news to channel"""
    with open('newsdata.json', 'r', encoding='utf-8') as newsdata:
        get_news_data()
        newsfile = json.load(newsdata)
        articles = len(newsfile["articles"])
        channel = discord.utils.get(ctx.guild.channels, name="news")
        today = str(datetime.date.today())
        await channel.send("**__News of " + today + "__**")
        for i in range(articles):
            await channel.send(embed=(format_news((newsfile["articles"])[i])))

client.run(TOKEN)
