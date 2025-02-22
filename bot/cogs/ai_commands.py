import discord
from discord.ext import commands
from bot.utils.permissions import is_bot_admin
import logging

logger = logging.getLogger(__name__)

class AICommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.model = None
        self.tokenizer = None

    async def setup_model(self):
        """Initialize the AI model and tokenizer"""
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
            import torch

            model_name = "aodev/mp"
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            logger.info(f"AI Model loaded successfully: {model_name}")
            return True
        except Exception as e:
            logger.error(f"Error loading AI model: {e}")
            return False

    @commands.command(name='chat')
    @is_bot_admin()
    async def chat(self, ctx, *, prompt: str):
        """Ai alapú csevegés (Alpha - Csak fejlesztőknek)"""
        if not self.model:
            success = await self.setup_model()
            if not success:
                await ctx.send("❌ Az AI modell nem tölthető be. Kérlek próbáld újra később.")
                return

        async with ctx.typing():
            try:
                # Encode the input text
                inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

                # Generate response
                outputs = self.model.generate(
                    inputs["input_ids"],
                    max_length=200,
                    num_return_sequences=1,
                    no_repeat_ngram_size=2,
                    temperature=0.7
                )

                # Decode and send response
                response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
                await ctx.send(f"🤖 {response}")
            except Exception as e:
                logger.error(f"Error in chat command: {e}")
                await ctx.send(f"❌ Hiba történt: {str(e)}")

    @commands.command(name='kép')
    @is_bot_admin()
    async def generate_image(self, ctx, *, prompt: str):
        """Ai alapú képet generál (Alpha - Csak fejlesztőknek)"""
        await ctx.send("🚧 Ez a funkció még fejlesztés alatt áll...")

    @commands.command(name='háttérkép')
    @is_bot_admin()
    async def generate_wallpaper(self, ctx, *, prompt: str):
        """Ai alapú háttérképet generál (Alpha - Csak fejlesztőknek)"""
        await ctx.send("🚧 Ez a funkció még fejlesztés alatt áll...")

    async def cog_command_error(self, ctx, error):
        """Error handler for the cog"""
        if isinstance(error, commands.CheckFailure):
            await ctx.send("❌ Ezt a parancsot csak a bot adminisztrátora használhatja!")
        else:
            logger.error(f"Error in AI command: {error}")
            await ctx.send(f"❌ Hiba történt: {str(error)}")

async def setup(bot):
    cog = AICommands(bot)
    await bot.add_cog(cog)