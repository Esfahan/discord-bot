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
    app.logger.error(error_msg)
    if os.environ.get('FLASK_ENV') != 'production':
        await ctx.send(error_msg)

@bot.command(brief='Check the connection', description='Check the connection')
async def ping(ctx):
    await ctx.send('Pong! Let\'s play Among Us!!')

@bot.command(brief='Display GitHUB URL', description='Show GitHUB URL')
async def github(ctx):
    await ctx.send('https://github.com/Esfahan/discord-bot')

@bot.command(brief='Register the impostor', description='Required:\nimpostor=impostor\'s name as an impostor\nwin_flg=0 is lose, 1 is win')
async def imp(ctx, impostor: str, win_flg: bool):
    app.logger.info(f'bot.user, {bot.user}')
    app.logger.info(f'bot.user.name, {bot.user.name}')
    app.logger.info(f'bot.user.id, {bot.user.id}')
    app.logger.info(f'ctx.author.name, {ctx.author.name}')
    app.logger.info(f'ctx.author.id, {ctx.author.id}')
    app.logger.info(f'impostor, {impostor}')
    app.logger.info(f'win_flg, {win_flg}')

    rc = ResultsController()
    await ctx.send(rc.impostor(impostor, win_flg, ctx.author.name, ctx.author.id, ''))

@bot.command(pass_context=True, brief='Display the impostors', description='Optional:\nlimit=int (0 means all)\norder_by=asc or desc')
async def results(ctx, limit: int=None, order_by: str=None):
    app.logger.info(f'bot.user, {bot.user}')
    app.logger.info(f'bot.user.name, {bot.user.name}')
    app.logger.info(f'bot.user.id, {bot.user.id}')
    app.logger.info(f'ctx.author, {ctx.author}')
    app.logger.info(f'ctx.author.id, {ctx.author.id}')
    app.logger.info(f'limit, {limit}')
    app.logger.info(f'limit, {order_by}')

    rc = ResultsController()
    results = rc.results(limit, order_by)

    if results:
        for result in results:
            await ctx.send(result)
    else:
        await ctx.send('No record')


bot.run(token)
