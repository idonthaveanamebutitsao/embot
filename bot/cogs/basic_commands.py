import discord
from discord.ext import commands
import platform
from datetime import datetime

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='ping', aliases=['kapcsolat'])
    async def ping(self, ctx):
        """Ellenőrzi a bot késleltetését"""
        latency = round(self.bot.latency * 1000)  # Convert to milliseconds
        await ctx.send(f'Pong! Késleltetés: {latency}ms')

    @commands.command(name='info', aliases=['információ'])
    async def info(self, ctx):
        """Információkat jelenít meg a botról"""
        embed = discord.Embed(
            title="Bot Információk",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )

        embed.add_field(name="Bot Neve", value=self.bot.user.name, inline=True)
        embed.add_field(name="Python Verzió", value=platform.python_version(), inline=True)
        embed.add_field(name="Discord.py Verzió", value=discord.__version__, inline=True)
        embed.add_field(name="Szerverek Száma", value=len(self.bot.guilds), inline=True)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(BasicCommands(bot))