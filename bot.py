import os
import giphy
import stocks
import discord
import typing
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

# Make sure the data subdirectory exists
Path('./data').mkdir(parents=True, exist_ok=True)

# Load our environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
NEXTCLOUD = os.getenv('NEXTCLOUD_URL')

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@bot.command()
async def ping(context):
    await context.channel.send('pong')


@bot.command(pass_context=True)
async def change_nickname(context, member: discord.Member, *args):
    new_nickname = ' '.join(args)
    await member.edit(nick=new_nickname)
    await context.send(f'{member}\'s nickname is now {new_nickname}.')


@bot.command()
async def gif(context, *args):
    query = '+'.join(args)
    url = giphy.search(query, 10)
    await context.send(url)


@bot.command()
async def google(context, *args):
    await context.send('https://www.google.com/')


@bot.command()
async def nextcloud(context):
    await context.channel.send(NEXTCLOUD)


@bot.command()
async def price_history(context,
                        symbol: typing.Optional[str] = 'VOO',
                        period: typing.Optional[str] = '1d',
                        interval: typing.Optional[str] = '1m'):

    filename = stocks.create_price_history_plot_png(symbol, period, interval)

    if filename != '':
        await context.send(file=discord.File(filename))
        stocks.delete_price_history_plot_png(filename)
    else:
        await context.send(f'{symbol}: No data found, symbol may be delisted.')


if __name__ == '__main__':
    bot.run(TOKEN)
