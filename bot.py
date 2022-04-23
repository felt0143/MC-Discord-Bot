# bot.py
import os

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
async def change_nickname(context, member: discord.Member, new_nickname):
    await member.edit(nick=new_nickname)
    await context.send(f'{member}\'s nickname is now {new_nickname}.')

bot.run(TOKEN)
