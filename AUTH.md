# Authentication Setup Guide for EmBot

## Required Accounts and Tokens

### 1. Discord Account & Bot Token (Already Set Up)
Your Discord bot token is already configured in the `.env` file.

### 2. HuggingFace Account
1. Create an account at https://huggingface.co/join
2. Generate an API token at https://huggingface.co/settings/tokens
3. Set the token in your environment variables (Already prompted)

### 3. GitHub Account Setup
1. Create a GitHub account at https://github.com/signup
2. Create a new repository:
   - Go to https://github.com/new
   - Name: `embot`
   - Description: "A versatile Discord bot with AI capabilities"
   - Choose "Public" repository
   - Initialize with a README
   - Add .gitignore for Python

### 4. bot-hosting.net Setup
1. Create an account at bot-hosting.net
2. Once logged in:
   - Click "Create New Bot"
   - Select "Import from GitHub"
   - Connect your GitHub account
   - Select the `embot` repository
   - Add environment variables:
     - `DISCORD_TOKEN`
     - `HUGGINGFACE_API_TOKEN`

## Connecting Everything Together

### Step 1: Push Code to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 2: Deploy on bot-hosting.net
1. After connecting GitHub, bot-hosting.net will automatically detect your repository
2. Configure your environment variables in bot-hosting.net's dashboard
3. Deploy your bot

### Step 3: Verify Everything
1. Check Discord: Bot should be online
2. Test commands: Try basic commands like `%help`
3. Test AI features: Try `%chat` command (admin only)

## Troubleshooting

If you encounter any issues:
1. Verify all tokens are correctly set in bot-hosting.net's environment variables
2. Check bot-hosting.net's logs for any errors
3. Ensure your Discord bot token is valid
4. Verify HuggingFace API token has proper permissions

Need help? Create an issue on GitHub or contact the respective platform's support:
- Discord: https://support.discord.com
- HuggingFace: https://huggingface.co/support
- bot-hosting.net: Support through their dashboard
