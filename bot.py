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
from copy import deepcopy
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents)
def delete():
    global f
    del f
monsters = []
quirks = []
classes = []
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
class class_char:
    def __init__(self,name,max_hp,dodge,prot,spd,acc_mod,crit,dmg_min,dmg_max,stun,blight,disease,move,bleed,debuff,trap,death_blow):
        self.name = name
        self.max_hp = max_hp
        self.dodge = dodge
        self.prot = prot 
        self.spd = spd
        self.acc_mod = acc_mod 
        self.crit = crit 
        self.dmg_min = dmg_min 
        self.dmg_max = dmg_max
        self.stun = stun 
        self.blight = blight
        self.disease = disease 
        self.move = move 
        self.bleed = bleed 
        self.debuff = debuff 
        self.trap = trap 
        self.death_blow = death_blow
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
quirks.append(quirk('beast_hater','positive',['+0.15 dmg','-0.15 beast_stress']))
classes.append(class_char('vestal',24,0,0,4,0,0.01,4,8,0.3,0.3,0.3,0.3,0.4,0.3,0.1,0.67))
classes.append(class_char('shieldbreaker',20,8,0,5,0,0.06,5,10,0.5,0.2,0.3,0.5,0.3,0.3,0.2,0.67))
classes.append(class_char('abomination',26,7.5,0,7,0,0.02,6,11,0.4,0.6,0.2,0.4,0.3,0.2,0.1,0.67))
classes.append(class_char('antiquarian',17,10,0,5,0,0.01,3,5,0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.67))
classes.append(class_char('arbalest',27,0,0,3,0,0.06,4,8,0.4,0.3,0.3,0.4,0.3,0.3,0.1,0.67))
classes.append(class_char('bounty_hunter',25,5,0,5,0,0.04,5,10,0.4,0.3,0.2,0.4,0.3,0.3,0.4,0.67))
classes.append(class_char('crusader',33,5,0,1,0,0.03,6,12,0.4,0.3,0.3,0.4,0.3,0.3,0.1,0.67))
classes.append(class_char('flagellant',22,0,0,6,0,0.02,3,6,0.5,0.3,0.4,0.5,0.65,0.3,0.0,0.73))
classes.append(class_char('grave_robber',20,10,0,8,0,0.06,4,8,0.2,0.5,0.3,0.2,0.3,0.3,0.5,0.67))
classes.append(class_char('hellion',26,10,0,4,0,0.05,6,12,0.4,0.4,0.3,0.4,0.4,0.3,0.2,0.67))
classes.append(class_char('highwayman',23,10,0,5,0,0.05,5,10,0.3,0.3,0.3,0.3,0.3,0.3,0.4,0.67))
classes.append(class_char('houndmaster',21,10,0,5,0,0.04,4,7,0.4,0.4,0.3,0.4,0.4,0.3,0.4,0.67))
classes.append(class_char('jester',19,15,0,7,0,0.04,4,7,0.2,0.4,0.2,0.2,0.3,0.4,0.3,0.67))
classes.append(class_char('leper',35,0,0,2,0,0.01,8,16,0.6,0.4,0.2,0.6,0.1,0.4,0.1,0.67))
classes.append(class_char('man-at-arms',31,5,0,3,0,0.02,5,9,0.4,0.3,0.3,0.4,0.4,0.3,0.1,0.67))
classes.append(class_char('musketeer',27,0,0,3,0,0.06,4,8,0.4,0.3,0.3,0.4,0.3,0.3,0.1,0.67))
classes.append(class_char('occultist',19,10,0,6,0,0.06,4,7,0.2,0.3,0.4,0.2,0.4,0.6,0.1,0.67))
classes.append(class_char('plague_doctor',22,0,0,7,0,0.02,4,7,0.2,0.6,0.5,0.2,0.2,0.5,0.2,0.67))
client = commands.Bot(command_prefix = '.', intents=intents)
global f
f = object()
@client.command()
async def Help(ctx):
    await ctx.channel.send('.fight *location* - starts a new fight in *location* [ruins,weald,warrens,cove]\n.retreat - retreats from the fight\n.show - shows the enemies\n.join name [quirks] (quirks must be in format: word_word if they consist of more than one, separated by ,)')
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
async def class_list(ctx):
    await ctx.channel.send("Names of classes:\nvestal\nshieldbreaker\nabomination\nantiquarian\narbalest\nbounty_hunter\ncrusader\nflagellant\ngrave_robber\nhellion\nhighwayman\nhoundmaster\njester\nleper\nman-at-arms\nmusketeer\noccultist\nplague_doctor \n(letter sizes doesn't matter)")
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
    new_im = Image.new('RGBA', (1000, 300))
    x_offset = 0
    back_width = 0
    for i in f.chars:
        imag = Image.open(i[1].name+'.png')
        new_im.paste(imag,(x_offset,150))
        x_offset += imag.size[0]
        back_width += imag.size[0]
    for im in images:
        width, height = im.size
        im=im.resize(((int)(width/3),(int)(height/3)))
        width, height = im.size
        back_width += width
        im=im.transpose(Image.FLIP_LEFT_RIGHT)
        new_im.paste(im, (x_offset,300-height))
        x_offset += im.size[0]
    back = Image.open(f.back+'.png')
    back = back.resize((1000,300))
    back = back.crop((0,0,back_width,300))
    
    back.paste(new_im,(0,0),new_im)
    back.save('fight.png')
    await ctx.channel.send(file=discord.File('fight.png'))
@client.command()
async def join(ctx,klass,name,quirks_char):
    quirks_char = quirks_char.strip('[')
    quirks_char = quirks_char.strip(']')
    array = quirks_char.split(',')
    if(len(array)>10):
        await ctx.channel.send("Too much quirks you liar")
    else:
        final = []
        good = 0
        bad = 0
        for i in range(len(array)):
            for quirk in quirks:
                if array == quirk.name:
                    final.append(quirk)
                    if quirk.type=='positive':
                        good+=1
                    else:
                        bad+=1
        for prof in classes:
            if prof.name == klass.lower():
                klass = prof
                break
        if(good>5 or bad>5):
            await ctx.channel.send("Too much quirks of one type")
        else:
            f.chars.append([ctx.author.id,deepcopy(klass),name,final])
            await show(ctx)
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
    testing.start()
