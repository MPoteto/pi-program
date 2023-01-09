
import json, os
os.system("title PI & color a")
f=open("conf.json")
ndata=json.load(f)

print("""

██████╗░██╗
██╔══██╗██║
██████╔╝██║
██╔═══╝░██║
██║░░░░░██║
╚═╝░░░░░╚═╝

Программа сделана с помощью poteto#2279

""")

while True:
    
    import datetime, time
    time.sleep(60)
    print("[PI] updating")
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    if len(str(minute)) == 1:
        minute = "0"+str(minute)
    print(hour, minute)
    
    for x in ndata["timers"]:
        print(x + "-" + str(hour) + ":" + str(minute))
        hm = str(hour) +":"+ str(minute)
        if x == hm:
            import discord
            from discord.ext import commands
            intents = discord.Intents.default()
            intents.members = True
            bot = commands.Bot(command_prefix="!", intents=intents)
            @bot.event
            async def on_ready():
                f = open("actions/"+ndata["timers"][str(x)]["actions_file"], "r")
                for i in f.readlines():
                    i = i.replace("\n", "")
                    if i.startswith("[wait]"):
                        cmd, sec = i.split(" ")
                        time.sleep(int(sec))
                    elif i.startswith("[activity]"):
                        try:
                            cmd, activity, text = i.split(" ", 2)
                            if activity == "game": actv = discord.Game(name=text)
                            if activity == "stream": actv = discord.Streaming(name=text, url='https://www.youtube.com/channel/UCe2gr26qwIdVpW_rdf0Jpfg')
                            if activity == "watch": actv = discord.Activity(type=discord.ActivityType.listening, name=text)
                            if activity == "listen": actv = discord.Activity(type=discord.ActivityType.watching, name=text)
                            else: actv = discord.Game(name="unavable")
                            await bot.change_presence(activity=actv)
                        except: pass
                    elif i.startswith("[status]"):
                        try:
                            cmd, activity = i.split(" ")
                            if activity == "online": await bot.change_presence(status=discord.Status.online)
                            if activity == "dnd": await bot.change_presence(status=discord.Status.dnd)
                            if activity == "idle": await bot.change_presence(status=discord.Status.idle)
                            if activity == "invisible": await bot.change_presence(status=discord.Status.invisible)
                            else: await bot.change_presence(status=discord.Status.online)
                        except: pass
                    elif i.startswith("[typing]"):
                        try:
                            cmd, channel, sec = i.split(" ")
                            async with bot.get_channel(int(channel)).typing():
                                import asyncio
                                await asyncio.sleep(int(sec))
                                                    
                        except: pass
                    elif i.startswith("[send]"):
                        cmd, ch, msg = i.split(" ", 2)
                        channel = bot.get_channel(int(ch))
                        await channel.send(msg)
            bot.run(ndata["token"], bot=False)
