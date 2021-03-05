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

@bot.command(brief='Checks the connection', description='Checks the connection')
async def ping(ctx):
    await ctx.send('Pong! Let\'s play Among Us!!')

@bot.command(brief='Shows GitHUB URL', description='Shows GitHUB URL')
async def github(ctx):
    await ctx.send('https://github.com/Esfahan/discord-bot')

@bot.command(brief='Shows Youtube URL', description='Shows Youtube URL')
async def youtube(ctx):
    await ctx.send('https://www.youtube.com/channel/UCeqPhExV09EF5o8lZLO15Eg')

@bot.command(brief='Shows Esfahan\'s profile', description='Shows Esfahan\'s profile')
async def profile(ctx):
    urls = ['Hello, I\'m Esfahan. Check my contents!',
            '[Twitter]\n<https://twitter.com/Esfahan0131>',
            '[GitHUB]\n<https://github.com/Esfahan>',
            '[Qiita]\n<https://qiita.com/Esfahan>',
            '[Youtube]\nGame: <https://www.youtube.com/channel/UCeqPhExV09EF5o8lZLO15Eg>\nCooking: <https://www.youtube.com/channel/UCDnYBh2TtUAfQ0Z-tl0jTyw>',
            '[cookpad]\n<https://cookpad.com/kitchen/13476667>']
    await ctx.send('\n\n'.join(urls))

@bot.command(brief='Registers the impostor', description='Required:\nimpostor=impostor\'s name as an impostor\nwin_flg=0 is lose, 1 is win')
async def imp(ctx, impostor: str, win_flg: bool, impostor02: str=None, win_flg02: bool=None, impostor03: str=None, win_flg03: bool=None):
    app.logger.info(f'bot.user, {bot.user}')
    app.logger.info(f'bot.user.name, {bot.user.name}')
    app.logger.info(f'bot.user.id, {bot.user.id}')
    app.logger.info(f'ctx.author.name, {ctx.author.name}')
    app.logger.info(f'ctx.author.id, {ctx.author.id}')
    app.logger.info(f'ctx.guild.id, {ctx.guild.id}')
    app.logger.info(f'ctx.channel, {ctx.channel}')
    app.logger.info(f'impostor, {impostor}')
    app.logger.info(f'win_flg, {win_flg}')
    app.logger.info(f'impostor02, {impostor02}')
    app.logger.info(f'win_flg02, {win_flg02}')
    app.logger.info(f'impostor03, {impostor03}')
    app.logger.info(f'win_flg03, {win_flg03}')

    rc = ResultsController()
    params = {'impostor': impostor,
              'win_flg': win_flg,
              'impostor02': impostor02,
              'win_flg02': win_flg02,
              'impostor03': impostor03,
              'win_flg03': win_flg03,
              'posted_user_name': ctx.author.name,
              'posted_user_id': ctx.author.id,
              'posted_server_id': ctx.guild.id}
    await ctx.send(rc.impostor(**params))

@bot.command(pass_context=True, brief='Shows the impostors', description='Optional:\nlimit=int (0 means all)\norder_by=asc or desc')
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
