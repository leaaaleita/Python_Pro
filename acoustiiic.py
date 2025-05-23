import discord
import random
from discord.ext import commands
import os
import requests
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='*', intents=intents)
@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} esta en linea')

@bot.command()
async def ayudaa(ctx):
    await ctx.send("""Comandos disponibles:
        "*hola - Saludo :D"
        "*significado - Significado de contaminación acústica."
        "*solucion - Te da una solución aleatoria para reducir la contaminación acústica."
        "*consejo - Un consejo ecológico para cuidar el medio ambiente y reducir el ruido."
        "*sd - Información sobre el impacto de la contaminación acústica en Santo Domingo."
        "*efectosneg - Efectos negativos de esta."
        "*sabiasque - Info valiosa"
        "*ayudaa - Muestra este mensaje de ayuda.""")

@bot.command()
async def hola(ctx):
    await ctx.send("Hola, soy Acoustic, y sé mucho sobre la contaminación acústica!")

@bot.command()
async def significado(ctx):
    await ctx.send("La contaminación acústica, aunque no la vemos, es una de las formas de deterioro ambiental más presentes en nuestras ciudades. También es una forma de contaminación que afecta directamente tanto al planeta como a nuestra salud física y mental.")

@bot.command()
async def sabiasque(ctx):
    await ctx.send ("Según la Organización Mundial de la Salud (OMS), los niveles de ruido no deberían superar los 55 decibeles (dB) durante el día ni los 40 dB por la noche. Pero en muchos sectores de Santo Domingo, especialmente cerca de colmadones, bares y zonas de alto tráfico, se registran niveles que superan los 80 dB. Esto equivale al ruido constante de una licuadora o una motocicleta, pero por muchísimo más tiempo.")

efectos = [
    "Problemas cardiovasculares",

"Ansiedad y depresión",

"Trastornos del sueño",

"Problemas de concentración (especialmente en niños)"]


@bot.command()
async def efectosneg(ctx):
    respuesta = random.choice(efectos)
    await ctx.send(respuesta)

sde = [
    "En Santo Domingo, afecta seriamente la salud y la calidad de vida de sus habitantes, especialmente en zonas con colmadones, tráfico intenso y construcciones ruidosas.",
    "Un estudio realizado por el Instituto Tecnológico de Santo Domingo (INTEC) en 2004 evaluó la calidad ambiental al interior de viviendas en tres barrios de la capital. Se midieron contaminantes como monóxido de carbono (CO), dióxido de nitrógeno (NO₂) y niveles de ruido. Los resultados indicaron que las condiciones de la vivienda influyen directamente en la calidad ambiental interior, afectando la seguridad, confort y salud de los habitantes.",
    ""
]
@bot.command()
async def sd(ctx):
    respuesta = random.choice(sde)
    await ctx.send(respuesta)

consejos = [
    "Si vas a escuchar música en casa, usa audífonos o mantén el volumen bajo, ¡tus vecinos lo agradecerán!",
    "Evita usar bocinas o altavoces potentes en la vía pública o residenciales.",
    "Los colmadones pueden funcionar sin ser escandalosos. Apoya a los que lo hacen bien.",
    "Si tienes un negocio, coloca letreros visibles que promuevan el respeto al silencio."
    ]

@bot.command()
async def consejo(ctx):
    respuesta = random.choice(consejos)
    await ctx.send(respuesta)



soluciones = [
    "✅ Regular horarios y volumen en colmadones, bares y discotecas.",
    "✅ Instalar sensores que midan niveles de ruido en tiempo real.",
    "✅ Participar en campañas de concientización sobre el ruido.",
    "✅ Exigir el cumplimiento de la Ley 64-00 sobre Medio Ambiente.",
    "✅ Promover el uso de aislamiento acústico en negocios ruidosos.",
    "✅ Fomentar el respeto a los espacios de silencio en zonas residenciales."
]
@bot.command()
async def solucion(ctx):
    respuesta = random.choice(soluciones)
    await ctx.send(respuesta)

token = ''
        
bot.run(token)