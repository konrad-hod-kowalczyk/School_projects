import discord
from discord.ext import commands
import random
import sys
from PIL import Image

client = commands.Bot(command_prefix = '.')
f = object()
images = [Image.open('Madman.png'),Image.open('Cultist_Acolyte.png'),Image.open('Cultist_Acolyte.png'),Image.open('Cultist_Acolyte.png')]
back = Image.open('ruins.png')
back = back.resize((600,300))
width,height = zip(*(i.size for i in images))
total_width = sum(width)
max_height = max(height)
monsters = []
def delete():
    f = object()
class fight_class:
    def __init__(self, choice):
        self.back=''
        if(choice.lower()=='ruins'):
            self.back='ruins'
        if(choice.lower()=='weald'):
            self.back='weald'
        if(choice.lower()=='warrens'):
            self.back='warrens'
        if(choice.lower()=='cove'):
            self.back='cove'
        else:
            print('shit')
    def __del__(self):
        print('The end')
class monster:
    def __init__(self, name, hp, dodge, protection, speed, stun, blight, bleed, debuff, move, loc):
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
        self.locations=[]
        for i in range(len(loc)):
            self.locations.append(loc[i])
monsters.append(monster('Bone_Rabble',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Webber',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Spitter',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Maggot',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Madman',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Brigand_Cutthroat',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Brigand_Fusilier',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Bloodletter',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Sycophant',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Supplicant',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Ghoul',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Cultist_Brawler',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Cultist_Acolyte',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Gargoyle',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Castellan',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Chevalier',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Rattler',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Cobra',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
monsters.append(monster('Big_Adder',8,0,0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove']))
@client.command()
async def fight(ctx, loc):
    f = fight_class(loc)
    delete()
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
@client.command()
async def monsterss(ctx):
    new_im = Image.new('RGBA', (total_width, max_height))
    x_offset = 0
    for im in images:
        im=im.resize((150,300))
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    back.paste(new_im,(0,0),new_im)
    back.save('fight.png')
    await ctx.channel.send(file=discord.File('fight.png'))
