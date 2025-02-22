from discord.ext import commands

def is_bot_admin():
    """
    Check if the user is a bot administrator
    """
    async def predicate(ctx):
        # Check if user has administrator permissions in the server
        if ctx.author.guild_permissions.administrator:
            return True
        # Check if user is the bot owner
        if await ctx.bot.is_owner(ctx.author):
            return True
        return False
    return commands.check(predicate)

def is_bot_owner():
    """
    Check if the user is the bot owner
    """
    async def predicate(ctx):
        return await ctx.bot.is_owner(ctx.author)
    return commands.check(predicate)
