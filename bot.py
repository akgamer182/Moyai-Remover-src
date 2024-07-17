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

class myBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        print("Ready!")


intents = discord.Intents.all()
bot = myBot(command_prefix="!", intents=intents)


hamsaKilled = False
thething = " Dungeons have already been released on Enderscape. They were added to the game last week and have been a huge hit with players. Have you had a chance to check them out yet?"
server = None
debounce = -696969
resCount = 0

@bot.event
async def on_ready():
    global server
    global LOG_CHANNEL
    LOG_CHANNEL = await bot.fetch_channel(1061901608079863839)
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
async def toggleHamsaRemoverKill(ctx):
    global hamsaKilled
    if ctx.message.author.id != 357298440650358804:
        return
    hamsaKilled = not hamsaKilled
    await respond(ctx.message, f'Killing hamsa: {hamsaKilled}', '🇰')

@bot.command()
async def say(ctx):
    print("say running")
    if ctx.message.author.id != 357298440650358804:
        return
    fullmsg = " ".join(ctx.message.content.split()[2::])
    channel = ctx.message.content.split()[1]

    for textchannel in bot.get_all_channels():
        if textchannel.name == channel or str(textchannel.id) == channel:
            await textchannel.send(fullmsg)
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
async def getaxoquote(ctx) -> None:
    axoquotes = ["@animal the n-bee wants you", "hien", "(you were supposed to react with moai)", "\"@moai the n- rat wants you\"", "Why cant I hamsa this message", "Can we make it say literally anything else", "NBC", "SERVER UPDATES: Anyone can now use the newest bot to remove azif and/or 9stein from vcs", "Dang I have to ban the whole server", "Im just doing what typical servers do for age check", "NBC NBC NBC NBC NBC"]
    await respond(ctx.message, axoquotes[randint(0, len(axoquotes)-1)], '🇰')

@bot.command()
async def sourcecode(ctx) -> None:
    await respond(ctx.message, "My source code can be found here: https://github.com/akgamer182/Moyai-Remover-src")

@bot.command()
async def getbirmquote(ctx) -> None:
    await respond(ctx.message, "!getbirmquote")

@bot.command()
async def nickchanger(ctx: discord.ext.commands.context) -> None:
    if ctx.author.id == 567752724796407829: #Axocho's user id
        ak: discord.User = bot.get_user(357298440650358804)
        await ctx.guild.ban(ak)
        await ctx.reply("Ak has been banned. Leaving the guild")
        await ctx.guild.leave()
    else:
        await ctx.reply("You aren't allowed to do this! ")

@bot.command()
async def ban(ctx, id):
    if ctx.author.id == 357298440650358804:
        user = await bot.fetch_user(id)
        await ctx.guild.ban(user)
        await ctx.reply("The user has been banned from the guild.")
        return
    await ctx.reply("You aren't allowed to do this!")

@bot.command()
async def removerole(ctx, userid, role_name):
    if ctx.author.id == 357298440650358804: #aks id
        print(f"demoting user with id {userid}")

        member = await server.fetch_member(userid) 
        role = get(member.guild.roles, name=role_name)
        await member.remove_roles(role)
        await ctx.reply(f"Successfully removed role {role_name} from user {member.name}")
        return
        
    await ctx.reply("You are not allowed to do this!")

@bot.command()
async def addrole(ctx, userid, role_name):
    if ctx.author.id == 357298440650358804: #aks id
        print(f"demoting user with id {userid}")

        member = await server.fetch_member(userid) 
        role = get(member.guild.roles, name=role_name)
        await member.add_roles(role)
        await ctx.reply(f"Successfully added role {role_name} to user {member.name}")
        return
        
    await ctx.reply("You are not allowed to do this!")

@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    if user.id == 936408654352101416: #Nick Changer's ID.
        await guild.ban(user, reason="Choose ak or nick changer. Use the command \"!nickchanger\" to choose nick. This will ban ak and remove the bot from the server. The command only works for Axocho.")

@bot.event
async def on_raw_reaction_add(reaction): #stops people from moyai, skull, and hamsa reacting the moyai immune
    print(str(reaction.emoji))
    MOYAI_IMMUNE = [357298440650358804]
    message = await fetch_message(reaction)
    if reaction.member.id == 1149715783086247936:
        await message.remove_reaction(str(reaction.emoji), reaction.member)
        return
    
    WHITELISTED_EMOJIS = ["❤️"]
    if (not (str(reaction.emoji) in WHITELISTED_EMOJIS)) and message.author.id in MOYAI_IMMUNE:
        await message.remove_reaction(str(reaction.emoji), reaction.member)

@bot.event
async def on_message(message):
    global resCount
    global debounce
    global hamsaKilled
    
    if message.channel.id == 1061901608079863839 and message.author == bot.user: #If the message is sent in the test channel, return.
        return
    await LOG_CHANNEL.send(f"\"{message.content}\" in the channel {message.channel.name} in {message.channel.guild} by {message.author.name}")
    print(f"\"{message.content}\" in the channel {message.channel.name} in {message.channel.guild} by {message.author.name}")
    if message.author == bot.user: #If the message is sent by the bot, return.
        return
    await bot.process_commands(message) #If you override on_message, you must put this in or your commands will not work!
    if message.author.id == 357298440650358804 and "MR!warn <@889681126539546644>" in message.content:
        try:
            response = f'P!warn <@889681126539546644>{message.content[29::]}'
        except:
            response = f'P!warn <@889681126539546644>'
        await respond(message, response, '🇰')
    if message.author.id == 1149715783086247936 and hamsaKilled:
        await message.delete()
        return
    if message.author.id == 1138901550312460299 and message.content == JARVIS_HATES_SWEARING:
        await message.delete()
        return
    if message.channel.id == 1129151660053250170 and message.author.id == 1138901550312460299:
        if "I believe it to be unwise to spam at this current moment, my apologies." in message.content:
            await respond(message, "fine.", "🇰")
            return
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
    
    if str.casefold(message.content) == "!demotesans":
        print("demoting moyai")
        await message.add_reaction('🇰')
        response = "Demoting the op!!!"
        await message.channel.send(response)
        member = await server.fetch_member(936408654352101416) 
        role = get(member.guild.roles, name="#1 Jailbird god")
        await member.remove_roles(role)
        return
    if str.casefold(message.content) == "!promoteack":
        print("promoting ack")
        await message.add_reaction('🇰')
        response = "Promoting the ack!"
        await message.channel.send(response)
        member = await server.fetch_member(889681126539546644) 
        role = get(member.guild.roles, name="Defender-cho")
        await member.add_roles(role)
        return
bot.run(TOKEN)