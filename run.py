import asyncio
from bot.main import run_bot
from bot.utils.logger import setup_logger

logger = setup_logger(__name__)

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        logger.info("Bot shutdown initiated by user")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
