import discord
from discord.ext import commands
import random
import asyncio
import os

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

tarea = None

# Lista de mensajes sobre el cambio climático
mensajes = [
    "La temperatura global ha aumentado 1,15°C por encima de los años 1850 a 1900.",
    "La última década ha sido la más cálida registrada a nivel mundial.",
    "Las actividades humanas, principalmente la quema de combustibles fósiles, han sido el principal motor del cambio climático desde el siglo XIX.",
    "El efecto invernadero es un proceso natural en el que ciertos gases atmosféricos atrapan el calor, vital para el sustento de la vida en la Tierra.",
    "Un 11 porciento de la población mundial (800 millones de personas) es actualmente vulnerable a los impactos del cambio climático.",
    "Desde el año 2000, más de 475.000 personas han muerto a causa de fenómenos meteorológicos extremos según el Índice de Riesgo Climático Global 2021.",
    "España se ubica en el puesto 29 en la lista de países que más han sufrido los efectos de los fenómenos meteorológicos extremos.",
    "2020 empató con 2016 como uno de los años más calurosos desde que se tienen registros.",
    "En los peores escenarios, el aumento de temperatura podría llegar a los 4,8 °C para finales de siglo.",
    "El 79 porciento de las emisiones de gases de efecto invernadero en la Unión Europea se deben a la quema de combustibles para usos energéticos o de transporte.",
    "En el Ártico, entre 1979 y 2014, desapareció el 40 porciento del área cubierta por el hielo marino.",
    "La tasa de subida del nivel del mar ascendió a 5 mm al año en el quinquenio 2014-2019.",
    "El cambio climático podría llevar hasta 132 millones de personas a la pobreza extrema en 2030.",
    "Los polos norte y sur se están calentando más rápido que el resto del mundo.",
    "La Antártida pierde enormes cantidades de hielo debido al calentamiento global.",
    "El nivel del mar ha subido aproximadamente 23 centímetros en el último siglo.",
    "Hasta un millón de especies están gravemente amenazadas por el cambio climático.",
    "Los 20 países más ricos son responsables de una gran parte de las emisiones de carbono.",
    "Las emisiones de gases de efecto invernadero han aumentado durante las últimas décadas.",
    "Más de 8 millones de personas mueren prematuramente cada año a causa de la contaminación provocada por los combustibles fósiles."
]


# Bucle de envío de mensajes
async def enviar(ctx):
    try:
        while True:
            mensaje = random.choice(mensajes)
            await ctx.send(mensaje)
            await asyncio.sleep(30)
    except asyncio.CancelledError:
        raise


# Comando para iniciar ($iniciar)
@bot.command()
async def iniciar(ctx):
    global tarea

    if tarea is not None and not tarea.done():
        await ctx.send("El bucle ya está funcionando.")
        return

    tarea = asyncio.create_task(enviar(ctx))
    await asyncio.sleep(5)


# Comando para detener ($detener)
@bot.command()
async def detener(ctx):
    global tarea

    if tarea is not None and not tarea.done():
        tarea.cancel()
        tarea = None
        await ctx.send("El bucle se ha detenido.")
    else:
        await ctx.send("El bucle no está funcionando.")


# Evento de conexión
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


# Iniciar el bot
bot.run("token")
