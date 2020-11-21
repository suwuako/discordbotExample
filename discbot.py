import discord
import nest_asyncio
from discord.ext import commands

class dsbot:
    def __init__(self):
        @bot.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(bot))

    def onMsg(self):
        @bot.event
        async def on_message(message):
            pass
            #this code runs whenever the bot reads/detects a message has been sent
    
    def commands(self):
        @bot.command
        async def commandName(message):
            pass    
    
    
    def run(self):
        
        bot.run('token-here')


if __name__ == '__main__':
    nest_asyncio.apply()
    bot = commands.Bot(command_prefix=';')
    dsbot = dsbot()
    dsbot.run()
