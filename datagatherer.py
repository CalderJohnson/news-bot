"""Module for the bot for gathering data"""
import json
import requests
import discord
from keys import API_KEY

#args

URL = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey='+API_KEY)

#get news daily

def get_news_data():
    """update newsdata.json"""
    response = requests.get(URL)
    with open('newsdata.json', 'w', encoding='utf-8') as newsdata:
        newsdata.truncate()
        json.dump(response.json(), newsdata)

#format news for printing

def format_news(article):
    """create embed for an article"""
    message = discord.Embed(title=article["title"], url=article["url"], description=article["description"])
    message.set_thumbnail(url=article["urlToImage"])
    return message
