import discord
import json
from discord.ext import commands
from discord_slash import SlashCommand


with open('not_token.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='r!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
  print('>>Bot is online<<')

@slash.slash(name='load', description='load')
async def load(ctx, extension):
  bot.load_extension(f'cmds.{extension}')
  await ctx.send(f'已載入 [{extension}] :white_check_mark:')

@slash.slash(name='unload', description='unload')
async def unload(ctx, extension):
  bot.unload_extension(f'cmds.{extension}')
  await ctx.send(f'已卸載 [{extension}] :white_check_mark:')

@slash.slash(name='reload', description='reload')
async def reload(ctx, extension):
  bot.reload_extension(f'cmds.{extension}')
  await ctx.send(f'已重載 [{extension}] :white_check_mark:')

@bot.event
async def on_command_error(ctx, error):
 await ctx.send(error)

if __name__ == "__main__":
  bot.run(jdata['TOKEN'])