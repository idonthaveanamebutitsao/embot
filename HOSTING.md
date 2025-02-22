# Hosting Instructions for EmBot

## GitHub Setup
1. Create a new GitHub repository at https://github.com/new
2. Initialize your local repository and push the code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin your-repository-url
git push -u origin main
```

## bot-hosting.net Setup
1. Create an account on bot-hosting.net
2. Click "Create New Bot"
3. Select "Import from GitHub"
4. Choose your repository
5. Add your environment variables:
   - DISCORD_TOKEN (your bot token)

## Important Notes
- Never commit your .env file to GitHub
- The bot will automatically use the DISCORD_TOKEN from bot-hosting.net's environment variables
- bot-hosting.net will automatically install dependencies from the installed packages

## Troubleshooting
If you encounter any issues:
1. Check the bot-hosting.net logs for errors
2. Verify your environment variables are set correctly
3. Ensure all dependencies are properly listed in the configuration

## Support
For hosting-related issues, contact bot-hosting.net support.
For bot-related issues, create an issue on the GitHub repository.
