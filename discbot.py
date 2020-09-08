# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:35:42 2020

@author: User
"""
import discord
import nest_asyncio
from discord.ext import commands

nest_asyncio.apply()
bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
@bot.event
async def on_message(message):
    pass
    #this code runs whenever the bot reads/detects a message has been sent
    
@bot.command
async def commandName(message):
    pass
    #this code runs whenever the bot reads ;commandName in chat because of [bot = commands.Bot(command_prefix=';')] and the command name being passed in async def
    
bot.run('bot token')
