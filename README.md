# EmBot Discord Bot

A versatile Discord bot with moderation, fun commands, and AI capabilities.

## Features

### Basic Commands
- Server management and information
- User information and avatars
- Embed message creation
- Daily messages
- Voting system

### Fun Commands
- Games (Number guessing, Rock Paper Scissors)
- Random activities (Coin flip, Dice roll)
- Math calculations
- Love meter and IQ calculator

### Moderation Commands
- Kick and ban management
- Message purging
- Channel management
- Ticket system

### AI Commands (Admin Only)
- AI-based chat interactions
- Image generation (Coming soon)
- Wallpaper generation (Coming soon)

## Setup Instructions

### Prerequisites
- Python 3.11+
- Discord Bot Token

### Local Development
1. Clone the repository
```bash
git clone https://github.com/yourusername/embot.git
cd embot
```

2. Create a .env file in the root directory:
```
DISCORD_TOKEN=your_discord_token_here
```

3. Install dependencies:
```bash
pip install discord.py python-dotenv torch transformers pillow aiohttp
```

4. Run the bot:
```bash
python run.py
```

### Hosting on bot-hosting.net
1. Create an account on bot-hosting.net
2. Create a new bot project
3. Connect your GitHub repository
4. Add your environment variables:
   - DISCORD_TOKEN
5. Deploy the bot

## Command Usage
Use `%help` to see all available commands and their descriptions.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
