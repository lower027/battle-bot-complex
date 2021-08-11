import asyncio
from discord.ext import commands
from discord.ext.commands import Cog 
from discord.ext.commands import command



wishwing1 = {}
wishwing2 = {}

bot = commands.Bot(command_prefix=".")

class stats(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command("input")
    async def stat_input(self, ctx):
        await ctx.send("Waiting for stats for Wishwing 1...")
        try:
            wishwing1["Name"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout.")
        
        try:
            wishwing1["Type"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")

        try:
            wishwing1["Attack"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")
        
        try:
            wishwing1["Magic"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")
        
        try:
            wishwing1["Defense"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")

        await ctx.send("Waiting for stats for Wishwing 2...")
        try:
            wishwing2["Name"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout.")
        
        try:
            wishwing2["Type"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")

        try:
            wishwing2["Attack"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")
        
        try:
            wishwing2["Magic"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")
        
        try:
            wishwing2["Defense"] = await self.bot.wait_for("message", timeout = 30.5)
        except asyncio.TimeoutError:
            await ctx.send("Timeout")


    @Cog.listener()

    async def on_ready(self):
        print("Stats cog ready!")

def setup(bot):
    bot.add_cog(stats(bot))