import discord
import COVID19Py

from discord.ext import tasks, commands

prefix = '/'

bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

covid19 = COVID19Py.COVID19(url='https://covid-tracker-us.herokuapp.com')

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def all(ctx):
    latest = covid19.getLatest()
    allEmbed = discord.Embed(title='Covid-19 information worldwide')
    allEmbed.add_field(name='Cases', value=latest['confirmed'])
    allEmbed.add_field(name='Deaths', value=latest['deaths'])
    allEmbed.add_field(name='Recovered', value=latest['recovered'])
    await ctx.send(embed=allEmbed)
    #get total num of cases/deaths/recovered

@bot.command()
async def allCases(ctx):
    latest = covid19.getLatest()
    allEmbed = discord.Embed(title='Covid-19 confirmed cases worldwide')
    allEmbed.add_field(name='Cases', value=latest['confirmed'])
    await ctx.send(embed=allEmbed)
    #get total num of cases/deaths/recovered

@bot.command()
async def allDeaths(ctx):
    latest = covid19.getLatest()
    allEmbed = discord.Embed(title='Covid-19 deaths worldwide')
    allEmbed.add_field(name='Deaths', value=latest['deaths'])
    await ctx.send(embed=allEmbed)
    #get total num of cases/deaths/recovered

@bot.command()
async def allRecovered(ctx):
    latest = covid19.getLatest()
    allEmbed = discord.Embed(title='Covid-19 recovered worldwide')
    allEmbed.add_field(name='Deaths', value=latest['recovered'])
    await ctx.send(embed=allEmbed)
    #get total num of cases/deaths/recovered

## --- COUNTRY SPECIFIC COMMANDS --- ##

@bot.command()
async def cases(ctx, country):
    casesByCountry = covid19.getLocationByCountryCode(country)
    casesEmbed = discord.Embed(title='Covid-19 confirmed cases')
    casesEmbed.add_field(name='Cases', value=casesByCountry[0]['latest']['confirmed'])
    await ctx.send(embed=casesEmbed)
    #get total num of confirmed cases for a country

@bot.command()
async def deaths(ctx, country):
    casesByCountry = covid19.getLocationByCountryCode(country)
    deathsEmbed = discord.Embed(title='Covid-19 confirmed deaths')
    deathsEmbed.add_field(name='Deaths', value=casesByCountry[0]['latest']['deaths'])
    await ctx.send(embed=deathsEmbed)
    #get total num of deaths
    
@bot.command()
async def recovered(ctx, country):
    casesByCountry = covid19.getLocationByCountryCode(country)
    recEmbed = discord.Embed(title='Covid-19 recovered in')
    recEmbed.add_field(name='Recovered', value=casesByCountry[0]['latest']['recovered'])
    await ctx.send(embed=recEmbed)
    #get total num of recovered

@bot.command()
async def help(message):
    helpC = discord.Embed(title="Covid-19 bot command guide", description="discord bot built for providing Covid-19 statistics")
    helpC.add_field(name="all", value="Displays data for cases, deaths and recovered worldwide", inline=False)
    helpC.add_field(name="allCases", value="Displays all cases", inline=False)
    helpC.add_field(name="allDeaths", value="Displays all deaths", inline=False)
    helpC.add_field(name="allRecovered", value="Displays all recovered", inline=False)
    helpC.add_field(name="cases <CountryCode>", value="Displays cases for a specific country", inline=False)
    helpC.add_field(name="deaths <CountryCode>", value="Displays deaths for a specific country", inline=False)
    helpC.add_field(name="recovered <CountryCode>", value="Displays recovered for a specific country", inline=False)
    await message.channel.send(embed=helpC)

bot.run('INSERT TOKEN HERE')
