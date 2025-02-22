import discord
from discord.ext import commands
from datetime import datetime

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kirúg valakit"""
        if reason is None:
            reason = "Nincs megadott indok"
        await member.kick(reason=reason)
        await ctx.send(f"{member.name} ki lett rúgva. Indok: {reason}")

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Kitiltasz valakit"""
        if reason is None:
            reason = "Nincs megadott indok"
        await member.ban(reason=reason)
        await ctx.send(f"{member.name} ki lett tiltva. Indok: {reason}")

    @commands.command(name='törlés')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Töröl valamennyi üzenetet"""
        if amount < 1:
            await ctx.send("Legalább 1 üzenetet meg kell adnod!")
            return
        deleted = await ctx.channel.purge(limit=amount + 1)  # +1 to include command message
        await ctx.send(f"{len(deleted)-1} üzenet törölve.", delete_after=5)

    @commands.command(name='hibajegy')
    async def ticket(self, ctx, *, reason=None):
        """Hibajegyet hozz létre"""
        if reason is None:
            await ctx.send("Kérlek adj meg egy indokot a hibajegyhez!")
            return

        # Create a new channel for the ticket
        guild = ctx.guild
        ticket_channel = await guild.create_text_channel(
            f'ticket-{ctx.author.name}',
            category=ctx.channel.category
        )

        # Set permissions
        await ticket_channel.set_permissions(ctx.guild.default_role, read_messages=False)
        await ticket_channel.set_permissions(ctx.author, read_messages=True, send_messages=True)

        # Send initial message in ticket channel
        embed = discord.Embed(
            title="Új Hibajegy",
            description=f"Hibajegy létrehozva {ctx.author.mention} által.\nIndok: {reason}",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        await ticket_channel.send(embed=embed)
        await ctx.send(f"Hibajegy létrehozva: {ticket_channel.mention}")

    @commands.command(name='zárás')
    async def close_ticket(self, ctx):
        """Hibajegy bezárása"""
        if not ctx.channel.name.startswith('ticket-'):
            await ctx.send("Ez nem egy hibajegy csatorna!")
            return

        await ctx.send("A hibajegy 5 másodperc múlva bezáródik...")
        await ctx.channel.delete(reason="Hibajegy lezárva")

    @commands.command(name='jelentés')
    async def report(self, ctx, *, content: str):
        """Jelentesz az EmBot fejlesztőinek hibát, ötletet stb."""
        embed = discord.Embed(
            title="Új Jelentés",
            description=content,
            color=discord.Color.yellow(),
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        await ctx.send("Köszönjük a jelentést! A fejlesztők hamarosan átnézik.", embed=embed)

async def setup(bot):
    await bot.add_cog(ModCommands(bot))