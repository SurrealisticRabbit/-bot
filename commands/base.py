import discord
from discord.ext import commands
from discord import app_commands

class BaseCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🏓 System Status",
            color=discord.Color.green(),
            timestamp=interaction.created_at
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.add_field(name="Latency", value=f"`{round(self.bot.latency * 1000)}ms`", inline=True)
        embed.add_field(name="Status", value=f"`{self.bot.status.name.title()}`", inline=True)
        embed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
