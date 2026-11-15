import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from game_logic import SinkingShipsGame

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class SinkingShipsView(discord.ui.View):
    def __init__(self, game: SinkingShipsGame):
        super().__init__(timeout=None)
        self.game = game

    def create_embed(self, message=""):
        sunk_count = self.game.get_sunk_count()
        grid_str = self.game.get_grid_string()
        status_text = f"**Squids Sunk:** {sunk_count}/3 | **Ammo:** {self.game.ammo}/30"
        
        embed = discord.Embed(
            title="🌊 Salvatore's Sinking Ships",
            description=f"{status_text}\n\n{message}\n```\n{grid_str}\n```",
            color=discord.Color.blue()
        )
        return embed

    @discord.ui.button(label="Left", style=discord.ButtonStyle.gray, emoji="⬅️")
    async def left(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.game.move_cursor(-1, 0)
        await interaction.response.edit_message(embed=self.create_embed())

    @discord.ui.button(label="Up", style=discord.ButtonStyle.gray, emoji="⬆️")
    async def up(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.game.move_cursor(0, -1)
        await interaction.response.edit_message(embed=self.create_embed())

    @discord.ui.button(label="Down", style=discord.ButtonStyle.gray, emoji="⬇️")
    async def down(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.game.move_cursor(0, 1)
        await interaction.response.edit_message(embed=self.create_embed())

    @discord.ui.button(label="Right", style=discord.ButtonStyle.gray, emoji="➡️")
    async def right(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.game.move_cursor(1, 0)
        await interaction.response.edit_message(embed=self.create_embed())

    @discord.ui.button(label="SHOOT", style=discord.ButtonStyle.danger, emoji="🔥")
    async def shoot(self, interaction: discord.Interaction, button: discord.ui.Button):
        result = self.game.shoot()
        
        if self.game.is_won():
            await interaction.response.edit_message(embed=self.create_embed(f"**{result}**\n🏆 **VICTORY!**"))
        elif "Out of ammo" in result:
            # Show revealed grid on loss
            revealed = self.game.get_revealed_grid()
            await interaction.response.edit_message(embed=discord.Embed(
                title="Game Over - Out of Ammo",
                description=f"**{result}**\n\nHere is where the squids were hiding:\n```\n{revealed}\n```",
                color=discord.Color.red()
            ))
        else:
            await interaction.response.edit_message(embed=self.create_embed(f"**{result}**"))

    @discord.ui.button(label="End", style=discord.ButtonStyle.secondary, emoji="❌")
    async def end(self, interaction: discord.Interaction, button: discord.ui.Button):
        revealed = self.game.get_revealed_grid()
        await interaction.response.edit_message(content=f"**Game Over!**\nHere is where the squids were:\n```\n{revealed}\n```", embed=None)
        self.stop()

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

bot = Bot()

@bot.tree.command(name="start_game", description="Start a new game")
async def start_game(interaction: discord.Interaction):
    game = SinkingShipsGame()
    view = SinkingShipsView(game)
    await interaction.response.send_message(embed=view.create_embed(), view=view)

bot.run(TOKEN)
