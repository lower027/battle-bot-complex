import asyncio
import numpy as np
import sys
import discord
from discord.ext.commands import command
from discord.ext.commands import Cog

wishwing1name = []
wishwing1types = []
wishwing1attack = []
wishwing1magic = []
wishwing1defense = []

wishwing2name = []
wishwing2types = []
wishwing2attack = []
wishwing2magic = []
wishwing2defense = []



class stats(Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @Cog.listener()

    async def on_ready(self):
        print("Stats cog ready!")

    @command(name = "input")

    async def stat_input(self, ctx):
        await ctx.send("Waiting for stats for Wishwing 1...")
    
        def check(message: discord.Message) -> bool:
            return message.author == ctx.author

        try:
             name = await self.bot.wait_for("message", timeout = 30.5, check = check)
        except asyncio.TimeoutError:
            await ctx.send("Timeout.")
        
        else:
            wishwing1name.append(str(name.content))
            await ctx.send(f"Name set to {name.content}")
        
            try:
                types = await self.bot.wait_for("message", timeout = 30.5, check = check)
            except asyncio.TimeoutError:
                await ctx.send("Timeout")

            else:
                wishwing1types.append(str(types.content))
                await ctx.send(f"Type set to {types.content}")

                try:
                    attack = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing1attack.append(int(attack.content))
                    await ctx.send(f"Attack set to {attack.content}")
                
                try:
                    magic = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                        await ctx.send("Timeout")
                    
                else:
                    wishwing1magic.append(int(magic.content))
                    await ctx.send(f"Magic set to {magic.content}")
        
                try:
                    defense = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                        
                else:
                    wishwing1defense.append(int(defense.content))
                    await ctx.send(f"Defense set to {defense.content}")


        await ctx.send("Waiting for stats for Wishwing 2...")
        try:
            name = await self.bot.wait_for("message", timeout = 30.5, check = check)
        except asyncio.TimeoutError:
            await ctx.send("Timeout.")

        else:
            wishwing2name.append(str(name.content))
            await ctx.send(f"Name set to {name.content}")
        
            try:
                types = await self.bot.wait_for("message", timeout = 30.5, check = check)
            except asyncio.TimeoutError:
                await ctx.send("Timeout")

            else:
                wishwing2types.append(str(types.content))
                await ctx.send(f"Type set to {types.content}")

                try:
                    attack = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing2attack.append(int(attack.content))
                    await ctx.send(f"Attack set to {attack.content}")
                
                try:
                    magic = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing2magic.append(int(magic.content))
                    await ctx.send(f"Magic set to {magic.content}")
                
                try:
                    defense = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing2defense.append(int(defense.content))
                    await ctx.send(f"Defense set to {defense.content}")
        


class Wishwing:
    def __init__(self, name, types, attack, magic, defense, health="===================="):
        #save variables as attributes
        self.name = name
        self.types = types
        self.attack = attack
        self.magic = magic
        self.defense = defense
        self.health = health
        self.bars = 20 #amount of health bars

class battle(Cog):
    def __init__(self, bot):
        self.bot = bot
    
       
    @Cog.listener()
    async def on_ready(self):
        print("Battle cog ready!")

   
    @command(name = "battle")    

    #setting up the fight

    async def fight(self, ctx, Wishwing2):

        #allow 2 Wishwings to fight each other.

        #Fight info
        await ctx.send("Wishwing Battle")
        await ctx.send(self.name)
        await ctx.send("\nTYPE/", self.types)
        await ctx.send("\nATTACK/", self.attack)
        await ctx.send("\nMAGIC/", self.magic)
        await ctx.send("\nDEFENSE/", self.defense)
        await ctx.send("\nLEVEL/", 2 * (1 + np.mean([self.attack, self.magic, self.defense])))
        await ctx.send("\nVS")
        await ctx.send(Wishwing2.name)
        await ctx.send("\nTYPE/", Wishwing2.types)
        await ctx.send("\nATTACK/", Wishwing2.attack)
        await ctx.send("\nMAGIC/", Wishwing2.magic)
        await ctx.send("\nDEFENSE/", Wishwing2.defense)
        await ctx.send("\nLEVEL/", 2 * (1 + np.mean([Wishwing2.attack, Wishwing2.magic, Wishwing2.defense])))

    #consider type advantages

        #lists of types and their weaknesses

        allignment = ["Light", "Dark", "Wind", "Ice", "Earth", "Steel", "Fire"]

        light_weakness = ["Dark", "Ice"]   
        dark_weakness = ["Light", "Fire"]    
        wind_weakness = ["Steel", "Ice"] 
        ice_weakness = ["Fire", "Steel"]
        earth_weakness = ["Ice", "Wind"]
        steel_weakness = ["Fire", "Earth"]
        fire_weakness = ["Earth", "Wind"]


        async for i,k in enumerate(allignment):
            if self.types == k:
                string_1_attack = await ctx.send("/nIt did normal damage.")
                string_2_attack = await ctx.send("/nIt did normal damage.")
            
            if self.types == light_weakness and Wishwing2.types == "Light":
                self.attack *= 2
                self.defense *= 2
                Wishwing2.attack /= 2
                Wishwing2.defense /= 2
                string_1_attack = await ctx.send("/nIt's very effective!")
                string_2_attack = await ctx.send("/nIt's not very effective....")

            if self.types == dark_weakness and Wishwing2.types == "Dark":
                self.attack *= 2
                self.defense *= 2
                Wishwing2.attack /= 2
                Wishwing2.defense /= 2
                string_1_attack = await ctx.send("/nIt's very effective!")
                string_2_attack = await ctx.send("/nIt's not very effective....")
            
            if self.types == wind_weakness and Wishwing2.types == "Wind":
                self.attack *= 2
                self.defense *= 2
                Wishwing2.attack /= 2
                Wishwing2.defense /= 2
                string_1_attack = await ctx.send("/nIt's very effective!")
                string_2_attack = await ctx.send("/nIt's not very effective....")
            
            if self.types == ice_weakness and Wishwing2.types == "Ice":
                self.attack *= 2
                self.defense *= 2
                Wishwing2.attack /= 2
                Wishwing2.defense /= 2
                string_1_attack = await ctx.send("/nIt's very effective!")
                string_2_attack = await ctx.send("/nIt's not very effective....")

            if self.types == earth_weakness and Wishwing2.types == "Earth":
                self.attack *= 2
                self.defense *= 2
                Wishwing2.attack /= 2
                Wishwing2.defense /= 2
                string_1_attack = await ctx.send("/nIt's very effective!")
                string_2_attack = await ctx.send("/nIt's not very effective....")
            
            if self.types == steel_weakness and Wishwing2.types == "Steel":
                self.attack *= 2
                self.defense *= 2
                Wishwing2.attack /= 2
                Wishwing2.defense /= 2
                string_1_attack = await ctx.send("/nIt's very effective!")
                string_2_attack = await ctx.send("/nIt's not very effective....")
            
            if self.types == fire_weakness and Wishwing2.types == "Fire":
                self.attack *= 2
                self.defense *= 2
                Wishwing2.attack /= 2
                Wishwing2.defense /= 2
                string_1_attack = await ctx.send("/nIt's very effective!")
                string_2_attack = await ctx.send("/nIt's not very effective....")

        
        #Fight
        #continue while each Wishwing still has health

        while (self.bars > 0) and (Wishwing2.bars > 0):
            await ctx.send(f"{self.health}\t\tHEALTH\t{self.health}")
            await ctx.send(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")

            await ctx.send(f"Go {self.name}!")

            #determine damage
            Wishwing2.bars -= (self.attack + self.magic)
            Wishwing2.health = ""

                #add back bars plus defense boost
            async for j in range(int(Wishwing2.bars + .1 * Wishwing2.defense)):
                Wishwing2.health = "="
                await ctx.send(f"{self.health}\t\tHEALTH\t{self.health}")
                await ctx.send(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")   

                #check to see if Wishwing2 can still battle
            if Wishwing2.bars <= 0:
                await ctx.send(f"....{Wishwing2.name} cannot battle anymore!") 
                break

            #Wishwing 2 turn

            await ctx.send(f"{self.health}\t\tHEALTH\t{self.health}")
            await ctx.send(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")

            await ctx.send(f"Go {Wishwing2.name}!")

            #determine damage
            self.bars -= (Wishwing2.attack + Wishwing2.magic)
            self.health = ""

            #add back bars plus defense boost
            async for j in range(int(self.bars + .1 * self.defense)):
                self.health = "="
                await ctx.send(f"{self.health}\t\tHEALTH\t{self.health}")
                await ctx.send(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")   

            #check to see if self can still battle
            if self.bars <= 0:
                await ctx.send(f".... {self.name} cannot battle anymore!") 
                break

        if __name__ == "__main__":
            
            WishwingA = Wishwing(wishwing1name, wishwing1types, wishwing1attack, wishwing1magic, wishwing1defense)
            WishwingB = Wishwing(wishwing2name, wishwing2types, wishwing2attack, wishwing2magic, wishwing2defense)


        WishwingA.fight(WishwingB)

   


def setup(bot):
    bot.add_cog(battle(bot))
    bot.add_cog(stats(bot))
        


        