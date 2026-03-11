import discord

def message_embed(interaction: discord.Interaction, title: str, description: str, color: discord.Color):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
        timestamp=interaction.created_at
    )
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)
    return embed