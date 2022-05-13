import os
import giphy
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="$")


@bot.command()
async def ping(context):
    await context.channel.send("pong")


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

if __name__ == '__main__':
    bot.run(TOKEN)
