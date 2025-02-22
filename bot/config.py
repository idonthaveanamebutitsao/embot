import os
from dotenv import load_dotenv

# SECURITY WARNING: Never commit or share your Discord bot token!
# If the token is accidentally exposed:
# 1. Go to Discord Developer Portal
# 2. Reset the token immediately
# 3. Update the .env file with the new token
load_dotenv()

# Bot configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = '%'

# Logging configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'