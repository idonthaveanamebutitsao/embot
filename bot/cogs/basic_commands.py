import discord
from discord.ext import commands
import platform
from datetime import datetime
import random

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.daily_messages = [
            "Legyen csodálatos napod!",
            "Ma is egy új lehetőség!",
            "Hidd el magadban!",
            "Minden nap egy új kaland!",
            "Te vagy a legjobb!",
        ]

    @commands.command(name='commands', aliases=['parancsok'])
    async def commands_list(self, ctx):
        """Megjeleníti az összes elérhető parancsot"""
        embed = discord.Embed(
            title="### Helló, EmBot vagyok!",
            description="### Sok parancsom van, próbálj ki párat!",
            color=discord.Color.blue()
        )

        # Alap parancsok
        basic_commands = """
        --> %help | Megjeleníti a bot parancsait
        --> %botinfó | Megjeleníti a bot statisztikáit
        --> /embed-create | Embed formátumban küldi az üzenetet
        --> /embed-image | Embed formátumban küldi a képet
        --> %avatar | Egy felhasználó profilképe
        --> %szerverkép | A szerver képe
        --> %ping | A késleltetés ezredmásodpercben
        --> %napiüzi | Egy kedves üzenet naponta
        --> %szavazás {szöveg} | Szavazást indít
        --> %üzenet | A bot elküldi amit írtál
        --> %hibajegy (indok) | Hibajegyet hozz létre
        --> %zárás | Hibajegy bezárása
        --> %userinfó {user} | Egy felhasználó információi
        --> %csatornainfó | Egy csatorna információi
        --> %szerverinfó | Egy szerver információi
        --> %jelentés | Jelentesz az EmBot fejlesztőinek hibát, ötletet stb.
        --> %hírek | A bot új hírei
        --> %admininfó | Admin jogosultságod ellenőrzése
        --> %bdt | A bot fejlesztőcsapatának információi
        """
        embed.add_field(name="### Alap parancsok:", value=basic_commands, inline=False)

        # Fun parancsok
        fun_commands = """
        --> %idő | A mai pontos idő
        --> %macska | Random macskás kép
        --> %kutya | Random kutyás kép
        --> %pénzdobás | 50%-50% fej vagy írás
        --> %melegségi szint {user} | Kiméri mennyire meleg valaki
        --> %iq | Kimére valaki mennyire okos
        --> %szeretet {user} | Kiméri mennyire szeret téged valaki
        --> %ölelés {user} | Random animés ölelés
        --> %8ball | 8 válasz
        --> %számkitaláló | 1-100 között kell kitalálni egy számott
        --> %random százalék | Egy random szám
        --> %hack {user} | ,,Feltőrsz'' valakit
        --> %keresés {szöveg} | Google keresés
        --> %karakter {szöveg} | Egy minecraft karakter keresése
        --> %mcszerver {szöveg} | Egy minecraft szerver keresése
        --> %eredmény {szöveg} | Egy minecraft achivment szöveg
        --> %kpo {szöveg} | Kő, papír, olló játék
        --> %matek {szöveg} | Matematikai számolások
        --> %kaszinó | Kaszinós szerencse játék
        --> %dobás | Dobókockával való dobás
        """
        embed.add_field(name="### Fun parancsok:", value=fun_commands, inline=False)

        # AI parancsok - updated to show alpha/dev status
        ai_commands = """
        ⚠️ **ALPHA - Fejlesztői és Admin Parancsok** ⚠️
        --> %chat | Ai alapú csevegés (Alpha - Csak fejlesztőknek)
        --> %kép | Ai alapú képet generál (Alpha - Csak fejlesztőknek)
        --> %háttérkép | Ai alapú háttérképet generál (Alpha - Csak fejlesztőknek)

        Ezek a parancsok jelenleg fejlesztés alatt állnak és csak a bot fejlesztői
        és adminisztrátorai használhatják.
        """
        embed.add_field(name="### Ai parancsok (Alpha):", value=ai_commands, inline=False)

        # Moderációs parancsok
        mod_commands = """
        --> %kick {user} (indok) | Kirúg valakit
        --> %ban {user} (indok) | Kitiltasz valakit
        --> %törlés {mennyiség} | Töröl valamennyi üzenetet
        --> /csatorna-készítés | Csatornát készít
        --> /csatorna-törlés | Csatornát töröl
        """
        embed.add_field(name="### Moderációs parancsok:", value=mod_commands, inline=False)

        # Jelmagyarázat
        legend = """
        {user} | Egy felhasználó neve (kötelező)
        {mennyiség} | Egy valaminek a mennyisége (kötelező)
        {szöveg} | Egy üzenet a parancsba (kötelező)
        (indok) | Valamire egy indok (opcionális)
        """
        embed.add_field(name="### Jelmagyarázat:", value=legend, inline=False)

        await ctx.send(embed=embed)

    @commands.command(name='ping', aliases=['kapcsolat'])
    async def ping(self, ctx):
        """Ellenőrzi a bot késleltetését"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! Késleltetés: {latency}ms')

    @commands.command(name='botinfo', aliases=['botinfó'])
    async def botinfo(self, ctx):
        """Megjeleníti a bot statisztikáit"""
        embed = discord.Embed(
            title="Bot Információk",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        embed.add_field(name="Bot Neve", value=self.bot.user.name, inline=True)
        embed.add_field(name="Python Verzió", value=platform.python_version(), inline=True)
        embed.add_field(name="Discord.py Verzió", value=discord.__version__, inline=True)
        embed.add_field(name="Szerverek Száma", value=len(self.bot.guilds), inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='szerverinfo', aliases=['szerverinfó'])
    async def serverinfo(self, ctx):
        """Egy szerver információi"""
        guild = ctx.guild
        embed = discord.Embed(
            title=f"{guild.name} Információk",
            color=discord.Color.green()
        )
        embed.add_field(name="Tulajdonos", value=guild.owner, inline=True)
        embed.add_field(name="Tagok száma", value=guild.member_count, inline=True)
        embed.add_field(name="Létrehozva", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)

    @commands.command(name='userinfo', aliases=['userinfó'])
    async def userinfo(self, ctx, member: discord.Member = None):
        """Egy felhasználó információi"""
        member = member or ctx.author
        embed = discord.Embed(
            title=f"Felhasználói Információk - {member.name}",
            color=member.color
        )
        embed.add_field(name="Felhasználónév", value=member.name, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Csatlakozott", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Fiók létrehozva", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.set_thumbnail(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        """Egy felhasználó profilképe"""
        member = member or ctx.author
        embed = discord.Embed(title=f"{member.name} profilképe")
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='napiüzi')
    async def daily_message(self, ctx):
        """Egy kedves üzenet naponta"""
        message = random.choice(self.daily_messages)
        embed = discord.Embed(
            title="Napi Üzenet",
            description=message,
            color=discord.Color.gold()
        )
        await ctx.send(embed=embed)

    @commands.command(name='szavazás')
    async def vote(self, ctx, *, question):
        """Szavazást indít"""
        embed = discord.Embed(
            title="📊 Szavazás",
            description=question,
            color=discord.Color.blue()
        )
        embed.set_footer(text=f"Szavazás indítva: {ctx.author.name} által")

        message = await ctx.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')

    @commands.command(name='admininfo', aliases=['admininfó'])
    async def admininfo(self, ctx):
        """Megjeleníti az admin jogosultságaid"""
        is_admin = ctx.author.guild_permissions.administrator
        is_owner = await self.bot.is_owner(ctx.author)

        embed = discord.Embed(
            title="Admin Információk",
            color=discord.Color.blue() if is_admin or is_owner else discord.Color.red()
        )

        status = []
        if is_owner:
            status.append("🔱 Bot Tulajdonos")
        if is_admin:
            status.append("⚡ Szerver Admin")
        if not status:
            status.append("❌ Nem vagy admin")

        embed.add_field(
            name="Jogosultságok",
            value="\n".join(status),
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.command(name='bdt', aliases=['fejlesztőcsapat', 'devteam'])
    async def dev_team(self, ctx):
        """Megjeleníti a fejlesztőcsapat információit"""
        # Create the embed
        embed = discord.Embed(
            title="EmBot Fejlesztőcsapat",
            description="A bot fejlesztői csapatának tagjai:",
            color=discord.Color.gold()
        )

        # Bot Owner
        owner_id = 1000445421270863932
        try:
            owner = await self.bot.fetch_user(owner_id)
            embed.add_field(
                name="🔱 Bot Tulajdonos",
                value=f"{owner.name} (ID: {owner.id})",
                inline=False
            )
            embed.set_thumbnail(url=owner.display_avatar.url)
        except:
            embed.add_field(
                name="🔱 Bot Tulajdonos",
                value=f"ID: {owner_id}",
                inline=False
            )

        # Main Developer
        embed.add_field(
            name="👨‍💻 Fő Fejlesztő",
            value=f"{ctx.author.name} (ID: {ctx.author.id})",
            inline=False
        )

        # Additional info
        embed.add_field(
            name="📝 Megjegyzés",
            value="Az EmBot egy nyílt forráskódú projekt, amely folyamatosan fejlődik.",
            inline=False
        )

        embed.set_footer(text="Köszönjük, hogy az EmBotot használod!")
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(BasicCommands(bot))