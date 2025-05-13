import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} esta en linea')
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        mensaje = f'👋 Bienvenido/a {member.mention} a {guild.name}!'
        await guild.system_channel.send(mensaje)
    try:
        await member.send('Bienvenid@! Mi prefijo es $ y los comandos disponibles por el momento son:' \
        ' saludar(puedes mandar helpsaludar por el server para que veas las opciones)' \
        'ping(pong!)' \
        'emoji(genera un emoji al azar)')
    except discord.Forbidden:
        print(f"No pude enviar un DM a {member.name}. Quizás tenga los DMs desactivados.")
    
emojis = ['😄', '🎉', '🔥', '💀', '🌈', '😎', '🧠', '🚀', '👀', '✨']

@bot.command()
async def emoji(ctx):
    emoji_random = random.choice(emojis)
    await ctx.send(f'{emoji_random}')
@bot.command()
async def ping(ctx):
    await ctx.send ("Pong!")
@bot.command()
async def helpcmds(ctx):
    await ctx.send('Comandos disponibles por el momento: saludar, emoji')
@bot.command()
async def helpsaludar(ctx):
    await ctx.send("Los comandos disponibles para saludar son: hola, holi, buenas, klk... Si lo escribes mal me encargaré de escribirte por DM para ayudarte!")
@bot.command()
async def saludar(ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        await ctx.send('Hola, ¿cómo estás?')
        user = ctx.author
        await user.send('👀')
    elif mensaje == 'klk':
        
        await ctx.send('Klk, ¿todo bien?')
        user = ctx.author
        await user.send('KLK')
    elif mensaje == 'buenas':
            
        await ctx.send('Buenas, ¿qué tal?')
        user = ctx.author
        await user.send('Buenas!')
    
    elif mensaje == 'holi':
        await ctx.send('Holiii!^^, ¿cómo estás?')
        user = ctx.author
        await user.send('Holi, espero estes bien^^')
    
    else:
        
        await ctx.send('SALUDA BIEN!!!')
        user = ctx.author
        await user.send('Los comandos disponibles para $saludar son: hola, klk, buenas y holi, intenta de nuevo con alguno de esos!')



        
token = 'token'
        
bot.run(token)



