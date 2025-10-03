import discord
from discord.ext import commands
from model import get_clases
import os, random
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'Sistema en linea como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola! Soy {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name= attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("no has subido ninguna imagen, volvé a intentarlo")

bot.run("MTQxODcyOTU3Njg3NTY4ODAzNg.Guv2aF.awek7PoeCzrPc0O20zsyGpgfXR7erhSSCj9KI0")