import aiohttp
import random
import discord
from discord.ext import commands
from random import randint 
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    count_heh=int(count_heh)
    if count_heh<100:
        await ctx.send("he" * count_heh)
    else:
        await ctx.send("Çok fazla heh!")

@bot.command()
async def total(ctx,*args):
    total=0
    for num in args:
        total+=int(num)
    await ctx.send(total)

@bot.command()
async def math(ctx,process):
    await ctx.send(eval(process))
    """(12)*"""

@bot.command()
async def tahmin(ctx, s1=1, s2=100):

    dogru_sayi = random.randint(s1, s2)
    tahmin_hakki = 1 if (s2-s1) == 0 else (1 + (s2-s1).bit_length())

    await ctx.send(f"@{ctx.author} {s1} ile {s2} arasında bir sayı seçildi.")
    await ctx.send(f"@{ctx.author} {tahmin_hakki} tahmin hakkınız var")

    while tahmin_hakki > 0:
        tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
        kullanici_tahmini = tahmin_mesaji.content

        try:
            kullanici_tahmini = int(kullanici_tahmini)
        except :
            await ctx.send(f"@{ctx.author} Lütfen bir sayı girin.")
            continue
        
        tahmin_hakki -= 1
        if kullanici_tahmini == dogru_sayi:
            await ctx.send(f"@{ctx.author} Bildiniz! Tebrikler!")
            break
        elif kullanici_tahmini < dogru_sayi:
            await ctx.send(f"@{ctx.author} Bilgisayarın tahmini daha büyük")
            await ctx.send(f"{tahmin_hakki} hakkınız kaldı")
        else:
            await ctx.send(f"@{ctx.author} Bilgisayarın tahmini daha küçük")
            await ctx.send(f"@{ctx.author} {tahmin_hakki} hakkınız kaldı")
    else:
        await ctx.send(f"@{ctx.author} Hak bitti, doğru cevap {dogru_sayi}")

bot.run("MTIzNzgzOTAxNjgwODY3NzQwNw.GFvJKf.USFgdzIW43C6XWAIUbz2Rq3s_FrNccuPeyzUdE")
