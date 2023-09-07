import os
from random import randint
import discord
from dotenv import load_dotenv
from time import time
from discord.ext import commands
from discord.utils import get
from datetime import datetime, timezone
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

JARVIS_HATES_SWEARING = "<@357298440650358804> This is a server with young children in it, such as SirPortals. Please do not be using heavy swear words, or you will be removed by the moderation team."

async def respond(msg, response, reaction=None): #responds to the message with response 
    if reaction != None: #reaction will be none by default. If a reaction is passed in, it will be added to the message 
        await msg.add_reaction(reaction)
    await msg.reply(response)

# def last_day(month: int, year: int): 
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     if month != 2:
#         return 30
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             return 28
#         else:
#             return 29
#     return 28


class myBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(self.my_background_task())
    
    async def on_ready(self):
        print("Ready!")

    async def my_background_task(self):
        await self.wait_until_ready()
        while True:
            print(self.is_closed())
            print("running")
            DT = datetime.now(timezone.utc)
            channel = await self.fetch_channel(1142703505065398322)
            NoNeedChannel = await self.fetch_channel(1143636311459246110)
            t0 = time()
            if (DT.hour == 0 and DT.minute == 0):
                await NoNeedChannel.send("No need to ban me. Cuz y’all mf’s obviously can’t get over what happened that one time on the Vc. Which is stupid asf and childish. And idgaf if y’all think I’m racist etc. because I’m not. And you can think I am idc. But get your facts and shit straight. Cuz I’m leaving this server. And whoever I added as a friend I’m blocking your ass. So no need to ban me.")
            if (DT.hour % 2 == 0 and DT.minute == 0):
            #if (True): #this is for debug, use the first one when not
                await channel.send("<@&1142700126045999184> Please use /bump so that we can get new members")
                #await channel.send("Test")
                #switch to the second one when debugging lmao
            try:
                await asyncio.sleep(60-(time()-t0))
            except:
                print(f"Starting the next loop behind by {round(-1*(60-(time()-t0)), 1)} seconds")


intents = discord.Intents.all()
bot = myBot(command_prefix="!", intents=intents)



thething = " Dungeons have already been released on Enderscape. They were added to the game last week and have been a huge hit with players. Have you had a chance to check them out yet?"
server = None
debounce = -696969
resCount = 0
@bot.event
async def on_ready():
    global server
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    server = bot.get_guild(955897343004270662)


async def fetch_message(payload): #fetches a message given the payload
    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    return message

async def disconnect_member(id): #kicks a member from vc
    user = await server.fetch_member(id) 
    await user.move_to(None)

@bot.command(aliases=['disconnectmoyai', 'disconnectmoai'])
async def disconnectazif(ctx):
    global debounce
    response = "Removing Azif from the vc!"

    if debounce+45 > time(): #if the command is on cooldown, let the user know and return
        await respond(ctx.message, f'This command is currently on cooldown! You may use this again in {round(debounce+45-time(), 1)} seconds.', "❌")
        return
    
    if randint(1, 100) == 69: #Generates a random number between 1 and 100 and checks if its 69. If so, kick axo as well and set response to reflect that
        await disconnect_member(567752724796407829)
        response = "Removing Azif and/or Cho from the vc! "
    
    await disconnect_member(889681126539546644)
    await respond(ctx.message, response, '🇰')
    return

@bot.command()
async def blm(ctx): #kicks 9Stein and mochi from the vc
    racists = [841782231407001651, 1071868068323663952]
    for id in racists:
        await disconnect_member(id)
    await respond(ctx.message, "Removing the racists from the vc!", '🇰')
    return

@bot.command()
async def removegod(ctx): #kicks cheese from vc
    await disconnect_member(696893217097908305)
    await respond(ctx.message, "Removing god from the vc!", '🇰')

@bot.command()
async def getaxoquote(ctx) -> str:
    axoquotes = ["@animal the n-bee wants you", "hien", "(you were supposed to react with moai)", "\"@moai the n- rat wants you\"", "Why cant I hamsa this message", "Can we make it say literally anything else", "NBC", "SERVER UPDATES: Anyone can now use the newest bot to remove azif and/or 9stein from vcs", "Dang I have to ban the whole server", "Im just doing what typical servers do for age check", "NBC NBC NBC NBC NBC"]
    await respond(ctx.message, axoquotes[randint(0, len(axoquotes)-1)], '🇰')

@bot.event
async def on_raw_reaction_add(raw_reaction_thing_idfk): #stops people from moyai, skull, and hamsa reacting the moyai immune
    print(str(raw_reaction_thing_idfk.emoji))
    MOYAI_IMMUNE = [357298440650358804]
    AXOS_CUSTOM_MOYAIS = ["hamza", "akreaction"]
    message = await fetch_message(raw_reaction_thing_idfk)
    if (str(raw_reaction_thing_idfk.emoji) in ["💀", '\U0001faac', "🗿", "😠"] or str.casefold(raw_reaction_thing_idfk.emoji.name) in AXOS_CUSTOM_MOYAIS) and message.author.id in MOYAI_IMMUNE:
        await message.remove_reaction(str(raw_reaction_thing_idfk.emoji), raw_reaction_thing_idfk.member)


@bot.event
async def on_message(message):
    global resCount
    global debounce
    print(f"\"{message.content}\"")
    await bot.process_commands(message) #If you override on_message, you must put this in or your commands will not work!
    if message.author == bot.user: #If the message is sent by the bot, return.
        return
    if message.author.id == 357298440650358804 and "MR!warn <@889681126539546644>" in message.content:
        try:
            response = f'P!warn <@889681126539546644>{message.content[29::]}'
        except:
            response = f'P!warn <@889681126539546644>'
        await respond(message, response, '🇰')
    if message.author.id == 1138901550312460299 and message.content == JARVIS_HATES_SWEARING:
        await message.delete()
    if message.channel.id == 1129151660053250170 and message.author.id == 1138901550312460299:
        if resCount > 69:
            resCount = 0
            return
        resCount +=1
        await respond(message, "Jarvis is 🗿! (fuck)", '🗿')
        return
    if "when dungeons" in message.content:
        response = "<@" + str(message.author.id) + ">" + thething
        await respond(message, response, '🗿')
        return
    # if str.casefold(message.content) == "!demotemoyai":
    #     print("demoting moyai")
    #     await message.add_reaction('🇰')
    #     response = "Demoting the moyai!!!"
    #     await message.channel.send(response)
    #     member = await server.fetch_member(889681126539546644) 
    #     role = get(member.guild.roles, name="Defender-cho")
    #     await member.remove_roles(role)
    #     return
    # if str.casefold(message.content) == "!promotemoyai":
    #     print("promoting moyai")
    #     await message.add_reaction('🇰')
    #     response = "Promoting the moyai!"
    #     await message.channel.send(response)
    #     member = await server.fetch_member(889681126539546644) 
    #     role = get(member.guild.roles, name="Defender-cho")
    #     await member.add_roles(role)
    #     return
bot.run(TOKEN)