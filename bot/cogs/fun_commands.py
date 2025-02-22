import discord
from discord.ext import commands
import random
from datetime import datetime
import time

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='idő')
    async def time(self, ctx):
        """A mai pontos idő"""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        await ctx.send(f"🕒 A pontos idő: {current_time}")

    @commands.command(name='pénzdobás')
    async def coinflip(self, ctx):
        """50%-50% fej vagy írás"""
        result = random.choice(["Fej", "Írás"])
        await ctx.send(f"🪙 {result}!")

    @commands.command(name='szeretet')
    async def love(self, ctx, member: discord.Member = None):
        """Kiméri mennyire szeret téged valaki"""
        if member is None:
            await ctx.send("Kérlek adj meg egy felhasználót!")
            return
        love_percent = random.randint(0, 100)
        embed = discord.Embed(
            title="❤️ Szeretet Mérő ❤️",
            description=f"{ctx.author.name} és {member.name} szeretet szintje: {love_percent}%",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @commands.command(name='8ball')
    async def eight_ball(self, ctx, *, question: str):
        """8 válasz"""
        responses = [
            "Biztos.", "Határozottan igen.", "Kétségtelenül.",
            "Igen.", "Valószínűleg.", "A jelek szerint igen.",
            "Nem.", "Ne számíts rá.", "Nagyon kétséges.",
        ]
        await ctx.send(f"🎱 {random.choice(responses)}")

    @commands.command(name='iq')
    async def iq(self, ctx, member: discord.Member = None):
        """Kiméri valaki mennyire okos"""
        member = member or ctx.author
        iq = random.randint(60, 160)
        await ctx.send(f"🧠 {member.name} IQ szintje: {iq}")

    @commands.command(name='számkitaláló')
    async def number_guess(self, ctx):
        """1-100 között kell kitalálni egy számot"""
        number = random.randint(1, 100)
        await ctx.send("Gondoltam egy számra 1 és 100 között. Találd ki!")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        for i in range(5):
            try:
                guess = await self.bot.wait_for('message', check=check, timeout=30.0)
                guess_num = int(guess.content)

                if guess_num == number:
                    await ctx.send(f"🎉 Gratulálok! Eltaláltad! A szám {number} volt.")
                    return
                elif guess_num < number:
                    await ctx.send("Magasabb!")
                else:
                    await ctx.send("Alacsonyabb!")
            except TimeoutError:
                await ctx.send(f"Időtúllépés! A szám {number} volt.")
                return

        await ctx.send(f"Sajnos nem találtad ki! A szám {number} volt.")

    @commands.command(name='kpo')
    async def rps(self, ctx, choice: str = None):
        """Kő, papír, olló játék"""
        if choice is None:
            await ctx.send("Használat: %kpo <kő/papír/olló>")
            return

        choices = ["kő", "papír", "olló"]
        choice = choice.lower()

        if choice not in choices:
            await ctx.send("Érvénytelen választás! Használj: kő, papír vagy olló")
            return

        bot_choice = random.choice(choices)
        result = "Döntetlen!"

        if (choice == "kő" and bot_choice == "olló") or \
           (choice == "papír" and bot_choice == "kő") or \
           (choice == "olló" and bot_choice == "papír"):
            result = "Nyertél! 🎉"
        elif choice != bot_choice:
            result = "Vesztettél! 😢"

        await ctx.send(f"Te: {choice}\nÉn: {bot_choice}\n{result}")

    @commands.command(name='matek')
    async def math(self, ctx, *, expression: str):
        """Matematikai számolások"""
        try:
            # Biztonságos kiértékelés basic műveletekhez
            result = eval(expression, {"__builtins__": {}}, {"abs": abs})
            await ctx.send(f"🔢 {expression} = {result}")
        except:
            await ctx.send("Érvénytelen matematikai kifejezés!")

    @commands.command(name='dobás')
    async def roll(self, ctx):
        """Dobókockával való dobás"""
        result = random.randint(1, 6)
        dice_emojis = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
        await ctx.send(f"{dice_emojis[result]} Dobtál egy {result}-est!")

async def setup(bot):
    await bot.add_cog(FunCommands(bot))