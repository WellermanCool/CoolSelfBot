import time
import datetime
from time import sleep
import json
import random
import string
from os import system, name
import os
from discord.ext import commands
import colorama
import asyncio
import re
import urllib.parse 
import io
import aiohttp
import discord
import requests
from colorama import Fore
colorama.init()

bot = commands.Bot(command_prefix=("$"), self_bot=True)
token = "NzQyNDM1MjYxOTQxNTQ3MDA5.YmCCoQ.Ds4u4dPjpHK1n9MwqQ5yHSaRDLM"
@bot.event
async def on_message(message):
  await bot.process_commands(message)
@bot.event
async def on_ready():
  print(f"{Fore.YELLOW}Logged as {Fore.RED}{bot.user}")

bot.remove_command("help")



@bot.command(pass_context=True)
async def spam(ctx, arg1, *, arg2):
    arg = int(arg1)
    i = 1
    arg3 = arg2
    while i<= arg:
        await ctx.send(f'{arg2}')
        i+=1



@bot.command()
async def game(ctx, *, arg):
  game = arg
  await ctx.message.delete()
  await bot.change_presence(activity=discord.Game(name=f'{game}'))
  print(f"{Fore.YELLOW}Logged as {Fore.RED}{bot.user}")

@bot.command()
async def help(ctx):
    ctx.send("$spam - колво сообщений, текст  $game - текст (меняет активность)")


        
      
  
  
  
  
bot.run(token, bot = False)
