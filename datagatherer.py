"""Module for the bot for gathering data"""
import requests
import json
import discord
import os

#args

key = '59fe0571600c499c819ff5acf822d637'

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey='+key)

#get news daily

def get_news_data():
    response = requests.get(url)
    with open('newsdata.json', 'w') as newsdata:
        newsdata.truncate()
        json.dump(response.json(), newsdata)

#format news for printing

def format_news(article):
    message = discord.Embed(title=article["title"], url=article["url"], description=article["description"])
    message.set_thumbnail(url=article["urlToImage"])
    return message
