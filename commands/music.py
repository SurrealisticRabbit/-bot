import discord
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from discord.ext import commands
from discord import app_commands


class SpotifyCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.spotify_client_id = None
        self.spotify_client_secret = None
        self.spotify_redirect_uri = None
        self.spotify_scope = None
        self.sp = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                client_id=self.spotify_client_id,
                client_secret=self.spotify_client_secret,
                redirect_uri=self.spotify_redirect_uri,
                scope=self.spotify_scope
            )
        )
    
    # Untested
    async def _login_modal(self, interaction: discord.Interaction) -> discord.Embed:
        r = discord.Embed(
            title="🎵 Spotify Login",
            color=discord.Color.green(),
            timestamp=interaction.created_at,
            url=self.sp.auth_manager.get_authorize_url()
        )
        r.set_thumbnail(url=self.bot.user.display_avatar.url)
        return r
        
    @app_commands.command(name="spotify_login", description="Login to Spotify")
    async def spotify_login(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True, ephemeral=True)
        await interaction.edit_original_response(
            embed=await self._login_modal(interaction)
        )
        
    async def _get_spotify_status(self) -> str:
        pass
        
    @app_commands.command(name="spotify_status", description="Checks status")
    async def spotify_status(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True, ephemeral=True)
        r = discord.Embed(
            title="Spotify Status",
            color=discord.Color.green(),
            timestamp=interaction.created_at
        )
        r.add_field(name="Login Status", value="Not Logged")
        r.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)
        r.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        r.set_thumbnail(url=self.bot.user.display_avatar.url
        )
        await interaction.edit_original_response(
            embed=r
        )
        
    @app_commands.command(name="spotify_playback", description="Control Spotify playback")
    async def spotify_playback(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True, ephemeral=True)
        r = discord.Embed() # Embed controllable player?
        await interaction.edit_original_response(
            embed=r
        )
        

