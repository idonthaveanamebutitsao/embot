import discord
from discord.ext import commands
import asyncio
from bot.config import DISCORD_TOKEN, COMMAND_PREFIX
from bot.utils.logger import setup_logger

logger = setup_logger(__name__)

class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=COMMAND_PREFIX, intents=intents)

    async def setup_hook(self):
        """Load cogs and perform initial setup"""
        try:
            await self.load_extension('bot.cogs.basic_commands')
            logger.info("Alap parancsok betöltve")
        except Exception as e:
            logger.error(f"Hiba az alap parancsok betöltésekor: {e}")

    async def on_ready(self):
        """Called when the bot is ready and connected to Discord"""
        logger.info(f'Bejelentkezve mint {self.user.name} (ID: {self.user.id})')
        activity = discord.Game(name=f"{COMMAND_PREFIX}help a parancsokért")
        await self.change_presence(activity=activity)

    async def on_command_error(self, ctx, error):
        """Global error handler for command errors"""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"A parancs nem található. Használd a `{COMMAND_PREFIX}help` parancsot a lehetséges parancsok megtekintéséhez.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Nincs jogosultságod ehhez a parancshoz.")
        else:
            logger.error(f"Hiba történt a parancs végrehajtásakor: {error}")
            await ctx.send("Hiba történt a parancs végrehajtása közben.")

async def run_bot():
    """Initialize and run the bot"""
    try:
        bot = DiscordBot()
        await bot.start(DISCORD_TOKEN)
    except Exception as e:
        logger.error(f"Hiba a bot indításakor: {e}")
        raise