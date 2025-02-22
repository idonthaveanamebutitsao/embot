import discord
from discord.ext import commands
from bot.utils.permissions import is_bot_admin
import logging
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BlenderbotTokenizer, BlenderbotForConditionalGeneration
import os

logger = logging.getLogger(__name__)

class AICommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.model = None
        self.tokenizer = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"AI Commands initialized. Using device: {self.device}")

        # Cache directory for models
        self.cache_dir = os.path.join(os.getcwd(), "model_cache")
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            logger.info(f"Created model cache directory at {self.cache_dir}")

    async def setup_model(self):
        """Initialize the AI model and tokenizer"""
        if self.model is not None:
            logger.info("Model already loaded, reusing existing model")
            return True

        try:
            model_name = "facebook/blenderbot-400M-distill"
            logger.info(f"Starting to load model: {model_name}")

            # Load tokenizer first
            logger.info("Loading tokenizer...")
            self.tokenizer = BlenderbotTokenizer.from_pretrained(
                model_name,
                cache_dir=self.cache_dir,
                local_files_only=False
            )
            if not self.tokenizer:
                logger.error("Failed to load tokenizer")
                return False
            logger.info("Tokenizer loaded successfully")

            # Load model with specific configuration
            logger.info("Loading model...")
            self.model = BlenderbotForConditionalGeneration.from_pretrained(
                model_name,
                torch_dtype=torch.float32,
                low_cpu_mem_usage=True,
                cache_dir=self.cache_dir,
                local_files_only=False
            )

            if not self.model:
                logger.error("Failed to load model")
                return False

            self.model.to(self.device)
            logger.info(f"Model loaded successfully and moved to device: {self.device}")

            # Verify model loaded correctly
            try:
                logger.info("Verifying model...")
                test_input = self.tokenizer("Hello, how are you?", return_tensors="pt").to(self.device)
                with torch.no_grad():
                    test_output = self.model.generate(
                        test_input["input_ids"],
                        max_length=50,
                        num_return_sequences=1,
                        pad_token_id=self.tokenizer.pad_token_id
                    )
                test_response = self.tokenizer.decode(test_output[0], skip_special_tokens=True)
                logger.info("Model verification successful")
            except Exception as e:
                logger.error(f"Model verification failed: {str(e)}", exc_info=True)
                self.model = None
                self.tokenizer = None
                return False

            return True

        except Exception as e:
            logger.error(f"Error loading AI model: {str(e)}", exc_info=True)
            self.model = None
            self.tokenizer = None
            return False

    @commands.command(name='chat')
    @is_bot_admin()
    async def chat(self, ctx, *, prompt: str):
        """Ai alapú csevegés (Alpha - Csak fejlesztőknek)"""
        async with ctx.typing():
            try:
                if not self.model:
                    logger.info("Model not loaded, attempting to load...")
                    await ctx.send("🔄 Betöltöm az AI modellt, kérlek várj...")
                    success = await self.setup_model()
                    if not success:
                        await ctx.send("❌ Az AI modell nem tölthető be. Kérlek próbáld újra később.")
                        return

                logger.info(f"Processing chat prompt: {prompt[:50]}...")
                # Encode the input text
                inputs = self.tokenizer(
                    prompt,
                    return_tensors="pt",
                    max_length=512,
                    truncation=True,
                    padding=True
                ).to(self.device)

                # Generate response
                with torch.no_grad():
                    outputs = self.model.generate(
                        inputs["input_ids"],
                        max_length=100,
                        num_return_sequences=1,
                        no_repeat_ngram_size=2,
                        temperature=0.7,
                        pad_token_id=self.tokenizer.pad_token_id,
                        attention_mask=inputs["attention_mask"]
                    )

                # Decode and send response
                response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
                logger.info("Successfully generated response")
                await ctx.send(f"🤖 {response}")

            except Exception as e:
                error_msg = str(e)
                logger.error(f"Error in chat command: {error_msg}", exc_info=True)
                await ctx.send(f"❌ Hiba történt: {error_msg}")

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
            error_msg = str(error)
            logger.error(f"Error in AI command: {error_msg}", exc_info=True)
            await ctx.send(f"❌ Hiba történt: {error_msg}")

async def setup(bot):
    cog = AICommands(bot)
    logger.info("Setting up AI Commands cog")
    await bot.add_cog(cog)
    logger.info("AI Commands cog setup complete")