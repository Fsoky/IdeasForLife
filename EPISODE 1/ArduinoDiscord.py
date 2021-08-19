import discord
from discord.ext import commands
from pyfirmata import Arduino

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
board = Arduino("COM6")


@bot.event
async def on_ready():
	print("Bot connected")


@bot.command()
async def toggle(ctx, value: int):
	if value == 1:
		board.digital[13].write(1)
	else:
		board.digital[13].write(0)

bot.run("token")