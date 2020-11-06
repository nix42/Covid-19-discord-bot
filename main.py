import discord
import COVID19Py

from discord.ext import tasks, commands

prefix = '/'

bot = commands.Bot(command_prefix = prefix)

covid19 = COVID19Py.COVID19(url='https://covid-tracker-us.herokuapp.com')

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def all(ctx):
    await 
    #get total num of cases/deaths/recovered

@bot.command()
async def cases(ctx, message, country):
    pass
    #get total num of confirmed cases

@bot.command()
async def deaths(ctx, message, country):
    pass
    #get total num of deaths
    
@bot.command()
async def recovered(ctx, message, country):
    pass
    #get total num of recovered


bot.run('Nzc0MzAwODMyNDYzNTg1MzAw.X6Vx2A.IX0Ip79xusXL34yy2-EKJ_kY4mQ')
