import discord
from discord.ext import commands
import random
import sys
import time
from PIL import Image

def delete():
    global f
    del f
monsters = []
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
        for i in self.cmonsters:
            print(i.name)
    def __del__(self):
        print('The end')
class monster:
    def __init__(self, name, hp, dodge, protection, speed, stun, blight, bleed, debuff, move, loc,size):
        self.name = name
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
monsters.append(monster('Bone_Rabble',8,0.0,0.0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Webber',7,15.0,0.0,5,0.25,0.2,0.2,0.1,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Spitter',7,15.0,0.0,4,0.25,0.2,0.2,0.1,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Maggot',6,0.0,0.0,3,1.0,0.4,0.4,0.6,0.0,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Madman',14,20.0,0.0,9,0.1,0.1,0.1,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Brigand_Cutthroat',12,2.5,0.15,3,0.25,0.2,0.2,0.15,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Brigand_Fusilier',12,7.5,0.0,6,0.25,0.2,0.2,0.15,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Brigand_Bloodletter',35,0.0,0.0,1,0.5,0.2,0.2,0.15,0.75,['ruins','weald','warrens','cove'],2))
monsters.append(monster('Sycophant',12,10.0,0.0,10,0.15,0.8,0.15,0.4,0.05,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Supplicant',12,0.0,0.20,1,1.5,0.5,0.15,0.4,0.25,['ruins','weald','warrens','cove'],1))
#monsters.append(monster('Ghoul',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],2))
monsters.append(monster('Cultist_Brawler',15,0.0,0.0,5,0.25,0.2,0.2,0.15,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Cultist_Acolyte',13,12.5,0.0,7,0.25,0.2,0.2,0.4,0.1,['ruins','weald','warrens','cove'],1))
#monsters.append(monster('Gargoyle',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Castellan',12,21.0,0.0,5,0.5,0.6,0.25,0.5,0.5,['ruins','weald','warrens','cove'],1))
#monsters.append(monster('Chevalier',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Rattler',24,7.5,0.25,9,0.25,0.4,0.2,0.2,0.5,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Pliskin',12,12.0,0.1,6,0.25,0.8,0.1,0.2,0.25,['ruins','weald','warrens','cove'],1))
monsters.append(monster('Big_Adder',45,5.0,0.2,4,0.5,0.75,0.2,0.4,0.8,['ruins','weald','warrens','cove'],2))
client = commands.Bot(command_prefix = '.')
global f
f = object()
@client.event
async def on_ready():
    print('ready')
@client.command()
async def fight(ctx, loc):
    global f
    f = fight_class(loc)
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
@client.command()
async def retreat(ctx):
    delete()
@client.command()
async def show(ctx):
    images = []
    for i in f.cmonsters:
        images.append(Image.open(i.name+'.png'))
    new_im = Image.new('RGBA', (600, 300))
    x_offset = 0
    for im in images:
        width, height = im.size
        im=im.resize(((int)(width/3),(int)(height/3)))
        width, height = im.size
        new_im.paste(im, (x_offset,300-height))
        x_offset += im.size[0]
    back = Image.open(f.back+'.png')
    back = back.resize((600,300))

    back.paste(new_im,(0,0),new_im)
    back.save('fight.png')
    await ctx.channel.send(file=discord.File('fight.png'))
   
