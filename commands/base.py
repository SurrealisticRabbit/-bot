import discord
from discord.ext import commands
from discord import app_commands

class BaseCommands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @app_commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
        
