import discord
from discord.ext import commands,tasks
import random
import sys
import time
import asyncio
from PIL import Image
import datetime as dt
import calendar as cl
from copy import deepcopy
from discord import FFmpegPCMAudio

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')
def delete():
    global f
    f = object()
monsters = []
quirks = []
classes = []
def quicksort(tab,l,p):
    v = tab[int((l+p)/2)][1]
    i=l
    j=p
    while True:
        while tab[i][1]>v:
            i+=1
        while tab[j][1]<v:
            j-=1
        if i<=j:
            x=tab[i]
            tab[i]=tab[j]
            tab[j]=x
            i+=1
            j-=1
        if i>j:
            break
    if j > l:
        quicksort(tab,l,j)
    if i < p:
        quicksort(tab,i,p)
    return tab
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
            self.cmonsters.append(deepcopy(monsters[random.randint(0,len(monsters)-1)]))
            if(sum(c.size for c in self.cmonsters)>4):
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
        self.skills = []
class quirk:
    def __init__(self,name,type,effects):
        self.name=name
        self.type=type
        self.effects = []
        for effect in effects:
            effect = effect.split(' ')
            self.effects.append([float(effect[0]),effect[1]])
class class_char:
    def __init__(self,name,max_hp,dodge,prot,spd,acc_mod,crit,stun,blight,disease,move,bleed,debuff,trap,death_blow):
        self.name = name
        self.max_hp = max_hp
        self.dodge = dodge
        self.prot = prot 
        self.spd = spd
        self.acc_mod = acc_mod 
        self.crit = crit 
        self.stun = stun 
        self.blight = blight
        self.disease = disease 
        self.move = move 
        self.bleed = bleed 
        self.debuff = debuff 
        self.trap = trap 
        self.death_blow = death_blow
        self.skills = []
        self.stress=0
class skill:
    def __init__(self,name,type,ranks,target,dmg,dmg_mod,acc,crit_mod,effects):
        self.name = name
        self.type = type
        self.ranks = ranks
        self.target = target
        self.dmg = dmg
        self.dmg_mod = dmg_mod
        self.acc = acc 
        self.crit_mod = crit_mod
        self.effects = effects
monsters.append(monster('Bone_Rabble','unholy',8,0.0,0.0,1,0.1,0.1,2.0,0.15,0.1,['ruins','weald','warrens','cove'],1))
monsters[0].skills.append(skill('Bump in the night','melee',[1,2,3],[1,2],lambda: random.randint(2,5),0,62.5,0.02,None))
monsters[0].skills.append(skill('Tic-Toc','melee',[4],[1,2],lambda: random.randint(2,5),0,42.5,0.00,None))
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
classes.append(class_char('vestal',24,0,0,4,0,0.01,0.3,0.3,0.3,0.3,0.4,0.3,0.1,0.67))
classes.append(class_char('shieldbreaker',20,8,0,5,0,0.06,0.5,0.2,0.3,0.5,0.3,0.3,0.2,0.67))
classes.append(class_char('abomination',26,7.5,0,7,0,0.02,0.4,0.6,0.2,0.4,0.3,0.2,0.1,0.67))
classes.append(class_char('antiquarian',17,10,0,5,0,0.01,0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.67))
classes.append(class_char('arbalest',27,0,0,3,0,0.06,0.4,0.3,0.3,0.4,0.3,0.3,0.1,0.67))
classes.append(class_char('bounty_hunter',25,5,0,5,0,0.04,0.4,0.3,0.2,0.4,0.3,0.3,0.4,0.67))
classes.append(class_char('crusader',33,5,0,1,0,0.03,0.4,0.3,0.3,0.4,0.3,0.3,0.1,0.67))
classes.append(class_char('flagellant',22,0,0,6,0,0.02,0.5,0.3,0.4,0.5,0.65,0.3,0.0,0.73))
classes.append(class_char('grave_robber',20,10,0,8,0,0.06,0.2,0.5,0.3,0.2,0.3,0.3,0.5,0.67))
classes.append(class_char('hellion',26,10,0,4,0,0.05,0.4,0.4,0.3,0.4,0.4,0.3,0.2,0.67))
classes.append(class_char('highwayman',23,10,0,5,0,0.05,0.3,0.3,0.3,0.3,0.3,0.3,0.4,0.67))
classes.append(class_char('houndmaster',21,10,0,5,0,0.04,0.4,0.4,0.3,0.4,0.4,0.3,0.4,0.67))
classes.append(class_char('jester',19,15,0,7,0,0.04,0.2,0.4,0.2,0.2,0.3,0.4,0.3,0.67))
classes.append(class_char('leper',35,0,0,2,0,0.01,0.6,0.4,0.2,0.6,0.1,0.4,0.1,0.67))
classes.append(class_char('man-at-arms',31,5,0,3,0,0.02,0.4,0.3,0.3,0.4,0.4,0.3,0.1,0.67))
classes.append(class_char('musketeer',27,0,0,3,0,0.06,0.4,0.3,0.3,0.4,0.3,0.3,0.1,0.67))
classes.append(class_char('occultist',19,10,0,6,0,0.06,0.2,0.3,0.4,0.2,0.4,0.6,0.1,0.67))
classes.append(class_char('plague_doctor',22,0,0,7,0,0.02,0.2,0.6,0.5,0.2,0.2,0.5,0.2,0.67))
global f
f = object()
@client.command()
async def help(ctx,option=None):
    if(option=='fight'):
        embed = discord.Embed(title='fight',description='Darkest Dungeon Combat Simulator version: alpha 0.0.1',colour = discord.Colour.green())
        embed.add_field(name='fight *location*',value='starts a new fight in *location*',inline=True)
        embed.add_field(name='retreat',value='retreats from the fight',inline=True)
        embed.add_field(name='show',value='shows the composition of characters and enemies',inline=True)
        embed.add_field(name='join *name* *[quirks]*',value='join with chosen character, quirks must be one word each. For two words quirks use word_word. If no quirks write only []',inline=False)
        embed.add_field(name='rand',value='generates random party of 4',inline=True)
        embed.add_field(name='class_list',value='shows available classes',inline=True)
        embed.set_thumbnail(url='https://www.darkestdungeon.com/wp-content/uploads/2017/09/PAX-Wallpaper.jpg')
        embed.set_image(url='https://www.darkestdungeon.com/wp-content/uploads/2017/09/Town_Event_Promo_Desktop2.jpg')
        embed.set_footer(text='available locations: [ruins,weald,warrens,cove]')
        await ctx.channel.send(embed=embed)
    elif(option=='whispers'):
        embed = discord.Embed(title = 'Whispers :smiling_imp:',description = "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn",colour = discord.Colour.red())
        embed.add_field(name="Il'gynoth",value='Heart_of_corruption.mp3',inline=True)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='bot functionality',colour=discord.Colour.blue())
        embed.add_field(name='fight', value='```to see more type .help fight```',inline=True)
        embed.add_field(name='whispers', value='```to see more type .help whispers```',inline=True)
        await ctx.channel.send(embed=embed)
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
    embed = discord.Embed(title='classes',description="letter sizes don't matter",colour = discord.Colour.green())
    embed.add_field(name='```vestal```',inline=True)
    embed.add_field(name='```shieldbreaker```',inline=True)
    embed.add_field(name='```abomination```',inline=True)
    embed.add_field(name='```antiquarian```',inline=True)
    embed.add_field(name='```arbalest```',inline=True)
    embed.add_field(name='```bounty_hunter```',inline=True)
    embed.add_field(name='```crusader```',inline=True)
    embed.add_field(name='```flagellant```',inline=True)
    embed.add_field(name='```grave_robber```',inline=True)
    embed.add_field(name='```highwayman```',inline=True)
    embed.add_field(name='```houndmaster```',inline=True)
    embed.add_field(name='```jester```',inline=True)
    embed.add_field(name='```leper```',inline=True)
    embed.add_field(name='```man-at-arms```',inline=True)
    embed.add_field(name='```musketeer```',inline=True)
    embed.add_field(name='```occultist```',inline=True)
    embed.add_field(name='```plague_doctor```',inline=True)
    await ctx.channel.send(embed=embed)
@client.command()
async def retreat(ctx):
    delete()
    #+stress
    await ctx.channel.send('Party is retreating')
@client.command()
async def start(ctx):
    global f
    while(1):
        order = []
        for i in f.cmonsters:
            order.append([i,random.randint(0,8)+i.speed])
        for i in f.chars:
            order.append([i,random.randint(0,8)+i[1].spd])
        order = quicksort(order,0,len(order)-1)
        #for i in range(len(order)):
        #    print(order[i][1])
        #print('------------------')
@client.command()
async def show(ctx):
    images = []
    for i in f.cmonsters:
        images.append(Image.open(i.name+'.png'))
    new_im = Image.new('RGBA', (1000, 300))
    x_offset = 0
    back_width = 0
    for i in range(len(f.chars)-1,-1,-1):
        imag = Image.open(f.chars[i][1].name+'.png')
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
    for i in f.chars:
            print(i[2])
    back.paste(new_im,(0,0),new_im)
    back.save('fight.png')
    await ctx.channel.send(file=discord.File('fight.png'))
@client.command()
async def rand(ctx):
    for i in range(4):
        f.chars.append([ctx.author.id,deepcopy(random.choice(classes)),'test'+str(random.randint(0,10000)),[]])
    await show(ctx)
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
@client.command(pass_context=True)
async def whispers(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        await ctx.channel.send("Voice of Il'gynoth is playing...")
        voice.play(FFmpegPCMAudio('C:\\Users\\zaras\\Desktop\\koło\\PythON\\heart.mp3'))
        while voice.is_playing():
            await asyncio.sleep(0.1)
        await voice.disconnect()
        await ctx.channel.send("Voice of Il'gynoth has stopped")
    else:
        await ctx.channel.send('You are not on the voice channel')
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
    testing.start()
