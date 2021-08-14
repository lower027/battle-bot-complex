import asyncio
import numpy as np
import sys
import discord
from discord.ext.commands import command
from discord.ext.commands import Cog

wishwing1 = None  # name, type, attack, magic, defense, HP

wishwing2 = None  # name, type, attack, magic, defense, HP


class WishWing:
    def __init__(self, name, w_type, attack, magic, defense, hp):
        self.name = name
        self.type = all_types[w_type]
        self.attack = int(attack)
        self.magic = int(magic)
        self.defense = int(defense)
        self.hp = int(hp)

    def __repr__(self):
        return f"WishWing: name={self.name}, type={self.type}, attack={self.attack}, magic={self.magic}, defense={self.defense}, hp={self.hp}"


class stats(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Stats cog ready!")

    @command(name="input")
    async def stat_input(self, ctx):
        global wishwing1, wishwing2
        await ctx.send("Waiting for stats for Wishwing 1...")

        def check(message: discord.Message) -> bool:
            return message.author == ctx.author

        """WishWing1!!!"""
        try:
            name = await self.bot.wait_for("message", timeout=30.5, check=check)
            types = await self.bot.wait_for("message", timeout=30.5, check=check)
            attack = await self.bot.wait_for("message", timeout=30.5, check=check)
            magic = await self.bot.wait_for("message", timeout=30.5, check=check)
            defense = await self.bot.wait_for("message", timeout=30.5, check=check)
            health = await self.bot.wait_for("message", timeout=30.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Timeout.")

        else:
            wishwing1 = WishWing(str(name.content), str(types.content), str(attack.content), str(magic.content), str(defense.content), str(health.content))
            await ctx.send(f"wishwing set to {wishwing1}")

        """WishWing2!!!"""
        await ctx.send("Waiting for stats for Wishwing 2...")

        try:
            name = await self.bot.wait_for("message", timeout=30.5, check=check)
            types = await self.bot.wait_for("message", timeout=30.5, check=check)
            attack = await self.bot.wait_for("message", timeout=30.5, check=check)
            magic = await self.bot.wait_for("message", timeout=30.5, check=check)
            defense = await self.bot.wait_for("message", timeout=30.5, check=check)
            health = await self.bot.wait_for("message", timeout=30.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Timeout.")

        else:
            wishwing2 = WishWing(str(name.content), str(types.content), str(attack.content), str(magic.content), str(defense.content), str(health.content))
            await ctx.send(f"wishwing set to {wishwing2}")

                
class Type:
    def __init__(self, w_type, weak, strong):
        self.type = w_type
        self.weak = weak
        self.strong = strong

    def __str__(self):
        return self.type

    def __gt__(self, other):
        if other in self.strong:
            return True
        if other in self.weak:
            return False
        else:
            return None

    def __lt__(self, other):
        if other in self.strong:
            return False
        if other in self.weak:
            return True
        else:
            return None


all_types = {
    "Fire": Type("Fire", weak = ["Earth", "Wind"], strong = ["Ice", "Dark"]),
    "Light": Type("Light", weak=["Dark", "Ice"], strong=["Dark"]),
    "Dark": Type("Dark", weak=["Light, Fire"], strong = ["Light"]),
    "Wind": Type("Wind", weak = ["Steel", "Ice"], strong = ["Earth", "Fire"]),
    "Ice": Type("Ice", weak = ["Fire", "Steel"], strong = ["Light", "Wind"]),
    "Earth": Type("Earth", weak = ["Ice", "Wind"], strong = ["Steel", "Fire"]),
    "Steel": Type("Steel", weak = ["Fire", "Earth"], strong = ["Wind", "Ice"])
}

        


class battle(Cog):
    def __init__(self, bot):
        self.bot = bot
    
       
    @Cog.listener()
    async def on_ready(self):
        print("Battle cog ready!")

   
    @command(name = "battle")    

    #setting up the fight

    async def fight(self, ctx):

#         #allow 2 Wishwings to fight each other.
        
#       #Fight info
        await ctx.send("Wishwing Battle")
        await ctx.send(wishwing1)
        await ctx.send("VS")
        await ctx.send(wishwing2)

        
        #Fight
        #continue while each Wishwing still has health

        while wishwing1.hp> 0 and  wishwing2.hp> 0:
            await ctx.send(f"{wishwing1.name} HEALTH {wishwing1.hp}")
            await ctx.send(f"{wishwing2.name} HEALTH {wishwing2.hp}")

            await ctx.send(f"Go {wishwing1.name}!")
                    
                

            #determine damage
            if wishwing1.type > wishwing2.type is None:
                wishwing2.hp -= (wishwing1.attack + wishwing1.magic - (wishwing2.defense * .1))
            elif wishwing1.type > wishwing2.type is True:
                wishwing2.hp -= (wishwing1.attack*2 + wishwing1.magic*2 - (wishwing2.defense * .05))
            elif wishwing1.type > wishwing2.type is False:
                wishwing2.hp -= (wishwing1.attack*0.5 + wishwing1.magic*0.5 - (wishwing2.defense * .2))
            
            #check to see if wishwing2 can still battle

            if wishwing2.hp <= 0:
                await ctx.send(f"HEALTH {wishwing1.hp}")
                await ctx.send(f"HEALTH 0")
                await ctx.send(f"....{wishwing2.name} cannot battle anymore!") 
                break

            #Wishwing 2 turn

            await ctx.send(f"{wishwing1.name} HEALTH {wishwing1.hp}")
            await ctx.send(f"{wishwing2.name} HEALTH {wishwing2.hp}")

            await ctx.send(f"Go {wishwing2.name}!")

            #determine damage
            if wishwing2.type > wishwing1.type is None:
                wishwing1.hp -= (wishwing2.attack + wishwing2.magic - (wishwing1.defense * .1))
            elif wishwing2.type > wishwing1.type is True:
                wishwing1.hp -= (wishwing2.attack*2 + wishwing2.magic*2 - (wishwing1.defense * .05))
            elif wishwing2.type > wishwing1.type is False:
                wishwing1.hp -= (wishwing2.attack*0.5 + wishwing2.magic*0.5 - (wishwing2.defense * .2))  

            #check to see if self can still battle
            if wishwing1.hp <= 0:
                await ctx.send(f"HEALTH 0")
                await ctx.send(f"HEALTH {wishwing2.hp}")
                await ctx.send(f".... {wishwing1.name} cannot battle anymore!") 
                break

   


def setup(bot):
    bot.add_cog(battle(bot))
    bot.add_cog(stats(bot))
        


        