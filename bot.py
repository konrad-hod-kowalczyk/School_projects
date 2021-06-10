import discord
from discord.ext import commands,tasks
import sys
import time
import asyncio
@client.command(pass_context=True)
async def obecnosc(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        members = channel.members
        ids=[]
        for member in members:
            ids.append(member.display_name)
        ids = (str(dt.datetime.now().day)+'.'+str(dt.datetime.now().month)+'.'+str(dt.datetime.now().year)+'  '+str(dt.datetime.now().hour)+':'+str(dt.datetime.now().minute),ids)
        await ctx.channel.send(ids)
    else:
        await ctx.channel.send('Nie jesteś na spotkaniu')
@tasks.loop(minutes=1.0)
async def reminder():
    channel = client.get_channel(0)
    yy,mm,dd=dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day
    if(cl.weekday(yy,mm,dd)==3 and dt.datetime.now().hour==17 and dt.datetime.now().minute==30):
        await channel.send("@everyone")
        await channel.send("**Przypomnienie o spotkaniu koła**")
@tasks.loop(hours=1.0)
async def testing():
    channel = client.get_channel(0)
    role = discord.utils.get(channel.guild.members, name='Evile')
    #role = discord.utils.get(channel.guild.roles, name='Sekretarz')
    #await channel.send(f"{role.mention}")
@client.event
async def on_ready():
    print('ready')
    reminder.start()
    #testing.start()
client.run('token')
