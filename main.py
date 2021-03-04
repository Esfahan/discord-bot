# -*- coding:utf-8 -*-
from discord.ext import commands
import os
import traceback

import sys
sys.path.append("/app/amongus")

from amongus.app import app
from amongus.results_controller import ResultsController

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
  print("[Information]")
  print("Name: " + bot.user.name)
  print("Id: " + str(bot.user.id) + "\n")
  print("[System]")
  print("Successfully logged in.")

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    #await ctx.send(orig_error)

@bot.command(brief='Check the connection', description='Check the connection')
async def ping(ctx):
    await ctx.send('Pong! Let\'s play Among Us!!')

@bot.command(brief='/github - Show GitHUB URL', description='/github - Show GitHUB URL')
async def github(ctx):
    await ctx.send('https://github.com/Esfahan/discord-bot')

@bot.command(brief='/winner {username} - Register the winner', description='/winner {username} - Register the winner')
async def winner(ctx, winner:str):
    app.logger.info(f'bot.user, {bot.user}')
    app.logger.info(f'bot.user.name, {bot.user.name}')
    app.logger.info(f'bot.user.id, {bot.user.id}')
    app.logger.info(f'ctx.author.name, {ctx.author.name}')
    app.logger.info(f'ctx.author.id, {ctx.author.id}')
    app.logger.info(f'winner, {winner}')

    rc = ResultsController()
    await ctx.send(rc.winner(winner, ctx.author.name, ctx.author.id, ''))

@bot.command(brief='/results - Show the winners', description='/results - Show the winners')
async def results(ctx):
    app.logger.info(f'bot.user, {bot.user}')
    app.logger.info(f'bot.user.name, {bot.user.name}')
    app.logger.info(f'bot.user.id, {bot.user.id}')
    app.logger.info(f'ctx.author, {ctx.author}')
    app.logger.info(f'ctx.author.id, {ctx.author.id}')

    rc = ResultsController()
    for results in rc.results():
        await ctx.send(results)


bot.run(token)
