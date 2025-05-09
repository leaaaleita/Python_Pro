import discord
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

