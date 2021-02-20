import discord
import random
import asyncio
from discord.ext import commands
from discord import User
from keep_alive import keep_alive
from discord.ext.commands import Bot, guild_only
import datetime

bot_prefix = '.h '

TOKEN = "Nzg5NTM3NDMxNDkzNjczMDAx.X9zgCA.mFqP6u1fqEBAZHmTlOQs5d8snwI"


intents=intents=discord.Intents.all()
intents = discord.Intents()
intents.members = True

intents = discord.Intents(
messages=True, guilds=True, reactions=True, members=True)


client = commands.Bot(command_prefix=bot_prefix, help_command=None)


@client.command()
async def help(ctx):
    embed=discord.Embed(title="(NSFW) categories:", url="https://discordbotlist.com/bots/latent", color=0x0008ff)
    embed.set_image(url="https://cdn.discordapp.com/attachments/810496908094210088/812045788342779904/Ekran_Alnts.PNG")
    embed.add_field(name=".h sendporn:", value="Typing this command will send you porn pictures/gif. Does not work unless (NSFW) mode is turned on in channel settings", inline=False)
    embed.add_field(name=".h sendboob:", value="Typing this command will send you boob pictures/gif. Does not work unless (NSFW) mode is turned on in channel settings", inline=False)
    embed.add_field(name=".h sendhip:", value="Typing this command will send you hip pictures/gif. Does not work unless (NSFW) mode is turned on in channel settings", inline=False)
    embed.add_field(name=".h sendpussy:", value="Typing this command will send you pussy pictures/gif. Does not work unless (NSFW) mode is turned on in channel settings", inline=False)
    await ctx.send(embed=embed)







@client.command()
async def sendporn(ctx):
    if ctx.channel.is_nsfw():
        sayi = random.randint(100,900)
        embed=discord.Embed(color=0xff0000)
        embed.set_author(name=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url="http://porngif.it/gif/ze%20predu/0" + str(sayi) + ".gif")
        embed.set_footer(text="ᔕcryonicsᔕ#4301",icon_url="https://cdn.discordapp.com/attachments/804842041145425921/809469421017628672/Ekran_Alnts.PNG")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        await ctx.send("The **nsfw** mode is **turned** off on this channel. To use this command, you need to turn on nsfw mode in settings.")
    

    

@client.command()
async def sendhip(ctx):
    if ctx.channel.is_nsfw():
        sayi = random.randint(100,150)
        embed=discord.Embed(color=0xff0000)
        embed.set_author(name=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url="http://porngif.it/gif/kundicky/0" + str(sayi) + ".gif")
        embed.set_footer(text="ᔕcryonicsᔕ#4301",icon_url="https://cdn.discordapp.com/attachments/804842041145425921/809469421017628672/Ekran_Alnts.PNG")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        await ctx.send("The **nsfw** mode is **turned** off on this channel. To use this command, you need to turn on nsfw mode in settings.")


@client.command()
async def sendboob(ctx):
    if ctx.channel.is_nsfw():
        sayi = random.randint(1,300)
        embed=discord.Embed(color=0xff0000)
        embed.set_author(name=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url="http://porngif.it/gif/prsa/0" + str(sayi) + ".gif")
        embed.set_footer(text="ᔕcryonicsᔕ#4301",icon_url="https://cdn.discordapp.com/attachments/804842041145425921/809469421017628672/Ekran_Alnts.PNG")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        await ctx.send("The **nsfw** mode is **turned** off on this channel. To use this command, you need to turn on nsfw mode in settings.")


@client.command()
async def sendpussy(ctx):
    if ctx.channel.is_nsfw():
        sayi = random.randint(100,200)
        embed=discord.Embed(color=0xff0000)
        embed.set_author(name=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url="http://porngif.it/gif/kundicky/0" + str(sayi) + ".gif")
        embed.set_footer(text="ᔕcryonicsᔕ#4301",icon_url="https://cdn.discordapp.com/attachments/804842041145425921/809469421017628672/Ekran_Alnts.PNG")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        await ctx.send("The **nsfw** mode is **turned** off on this channel. To use this command, you need to turn on nsfw mode in settings.")
    



keep_alive()


client.run(TOKEN)