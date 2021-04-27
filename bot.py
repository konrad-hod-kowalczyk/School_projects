import discord
from discord.ext import commands
from discord.ext import tasks
import random
import sys
import time
import asyncio
from PIL import Image
import datetime as dt
import calendar as cl
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents)
def delete():
    global f
    del f
monsters = []
quirks = []
class fight_class():
    def __init__(self, choice):
        self.back=''
        if(choice.lower()=='ruins'):
            self.back='ruins'
        elif(choice.lower()=='weald'):
            self.back='weald'
        elif(choice.lower()=='warrens'):
            self.back='warrens'
        elif(choice.lower()=='cove'):
            self.back='cove'
        else:
            print('shit')
            delete()
        self.cmonsters = [];
        while(len(self.cmonsters)!=4):
            self.cmonsters.append(monsters[random.randint(0,len(monsters)-1)])
            if(self.back not in self.cmonsters[len(self.cmonsters)-1].locations or sum(c.size for c in self.cmonsters)>4):
                self.cmonsters.pop(len(self.cmonsters)-1)
                break
        self.chars = []
        for i in self.cmonsters:
            print(i.name)
    def __del__(self):
        print('The end')
class monster:
    def __init__(self, name, type, hp, dodge, protection, speed, stun, blight, bleed, debuff, move, loc,size):
        self.name = name
        self.type = type
        self.hp = hp
        self.dodge = dodge
        self.protection = protection
        self.speed = speed
        self.stun = stun 
        self.blight = blight 
        self.bleed = bleed 
        self.debuff = debuff 
        self.move = move
        self.skills=[]
        self.size = size
        self.locations=[]
        for i in range(len(loc)):
            self.locations.append(loc[i])
class quirk:
    def __init__(self,name,type,effects):
        self.name=name
        self.type=type
        self.effects = []
        for effect in effects:
            effect = effect.split(' ')
            self.effects.append([float(effect[0]),effect[1]])
monsters.append(monster('Bone_Rabble','unholy',8,0.0,0.0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Webber','beast',7,15.0,0.0,5,0.25,0.2,0.2,0.1,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Spitter','beast',7,15.0,0.0,4,0.25,0.2,0.2,0.1,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Maggot','beast',6,0.0,0.0,3,1.0,0.4,0.4,0.6,0.0,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Madman','human',14,20.0,0.0,9,0.1,0.1,0.1,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Brigand_Cutthroat','human',12,2.5,0.15,3,0.25,0.2,0.2,0.15,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Brigand_Fusilier','human',12,7.5,0.0,6,0.25,0.2,0.2,0.15,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Brigand_Bloodletter','human',35,0.0,0.0,1,0.5,0.2,0.2,0.15,0.75,['ruins','weald','warrens','cove'],2))
monsters.append(monster('Sycophant','bloodsucker',12,10.0,0.0,10,0.15,0.8,0.15,0.4,0.05,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Supplicant','bloodsucker',12,0.0,0.20,1,1.5,0.5,0.15,0.4,0.25,['ruins','weald','warrens','cove'],1))
#monsters.append(monster('Ghoul',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],2))
monsters.append(monster('Cultist_Brawler','human',15,0.0,0.0,5,0.25,0.2,0.2,0.15,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Cultist_Acolyte','human',13,12.5,0.0,7,0.25,0.2,0.2,0.4,0.1,['ruins','weald','warrens','cove'],1))
#monsters.append(monster('Gargoyle',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Castellan','bloodsucker',12,21.0,0.0,5,0.5,0.6,0.25,0.5,0.5,['ruins','weald','warrens','cove'],1))
#monsters.append(monster('Chevalier',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Rattler','beast',24,7.5,0.25,9,0.25,0.4,0.2,0.2,0.5,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Pliskin','beast',12,12.0,0.1,6,0.25,0.8,0.1,0.2,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Big_Adder','beast',45,5.0,0.2,4,0.5,0.75,0.2,0.4,0.8,['ruins','weald','warrens','cove'],2))
quirks.append(quirk('Beast Hater','positive',['+0.15 dmg','-0.15 beast_stress']))
client = commands.Bot(command_prefix = '.', intents=intents)
global f
f = object()
@client.command()
async def Help(ctx):
    await ctx.channel.send('.fight *location* - starts a new fight in *location* [ruins,weald,warrens,cove]\n.retreat - retreats from the fight\n.show - shows the enemies\n.join name [quirks], quirks must be in format: word_word if they consist of more than one')
@client.command()
async def fight(ctx, loc):
    delete()
    global f
    f = fight_class(loc)
    await show(ctx)
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
@client.command()
async def retreat(ctx):
    delete()
    #+stress
    await ctx.channel.send('Party is retreating')
@client.command()
async def show(ctx):
    images = []
    for i in f.cmonsters:
        images.append(Image.open(i.name+'.png'))
    new_im = Image.new('RGBA', (600, 300))
    x_offset = 0
    back_width = 0
    for im in images:
        width, height = im.size
        im=im.resize(((int)(width/3),(int)(height/3)))
        width, height = im.size
        back_width += width
        new_im.paste(im, (x_offset,300-height))
        x_offset += im.size[0]
    back = Image.open(f.back+'.png')
    back = back.resize((600,300))
    back = back.crop((0,0,back_width,300))
    
    back.paste(new_im,(0,0),new_im)
    back.save('fight.png')
    await ctx.channel.send(file=discord.File('fight.png'))
@client.command()
async def join(ctx,name,quirks_char):
    final = []
    good = 0
    bad = 0
    if(len(quirks_char)>10):
        await ctx.channel.send("Too much quirks you liar")
    else:
        for i in range(len(quirks_char)):
            for quirk in quirks:
                if quirks_char == quirk.name:
                    final.append(quirk)
                    if quirk.type=='positive':
                        good+=1
                    else:
                        bad+=1
        if(good>5 or bad>5):
            await ctx.channel.send("Too much quirks of one type")
        else:
            f.chars.append([ctx.author.id,name,quirks_char])
            await ctx.channel.send(f.chars)
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
    role = discord.utils.get(channel.guild.members, display_name='Konrad K')
    #role = discord.utils.get(channel.guild.roles, name='Sekretarz')
    #await channel.send(f"{role.mention}")
@client.event
async def on_ready():
    print('ready')
    reminder.start()
    testing.start()
