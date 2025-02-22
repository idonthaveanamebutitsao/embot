# GitHub Repository Setup Guide

Follow these steps to create and connect your GitHub repository:

1. Create a new GitHub repository:
   - Go to https://github.com/new
   - Repository name: `embot`
   - Description: "A versatile Discord bot with AI capabilities"
   - Choose "Public" repository
   - Initialize with README: No (we already have one)
   - Click "Create repository"

2. Initialize your local repository and push the code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_REPOSITORY_URL
   git push -u origin main
   ```

3. Verify your repository:
   - Check that all files are properly uploaded
   - Ensure sensitive files (.env) are not included
   - Confirm README.md and documentation are visible

4. Next Steps:
   Once your GitHub repository is set up, we'll connect it to bot-hosting.net.
