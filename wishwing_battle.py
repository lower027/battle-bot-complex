import asyncio
import numpy as np
import sys
import discord
from discord.ext.commands import command
from discord.ext.commands import Cog



wishwing1 = [] #name, type, attack, magic, defense, HP


wishwing2 = [] #name, type, attack, magic, defense, HP





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
            wishwing1.append(str(name.content))
            await ctx.send(f"Name set to {name.content}")
        
            try:
                types = await self.bot.wait_for("message", timeout = 30.5, check = check)
            except asyncio.TimeoutError:
                await ctx.send("Timeout")

            else:
                wishwing1.append(str(types.content))
                await ctx.send(f"Type set to {types.content}")

                try:
                    attack = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing1.append(int(attack.content))
                    await ctx.send(f"Attack set to {attack.content}")
                
                try:
                    magic = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                        await ctx.send("Timeout")
                    
                else:
                    wishwing1.append(int(magic.content))
                    await ctx.send(f"Magic set to {magic.content}")
        
                try:
                    defense = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                        
                else:
                    wishwing1.append(int(defense.content))
                    await ctx.send(f"Defense set to {defense.content}")
                
                try:
                    health = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing1.append(int(health.content))
                    await ctx.send(f"Health set to {health.content}")


        await ctx.send("Waiting for stats for Wishwing 2...")
        try:
            name = await self.bot.wait_for("message", timeout = 30.5, check = check)
        except asyncio.TimeoutError:
            await ctx.send("Timeout.")

        else:
            wishwing2.append(str(name.content))
            await ctx.send(f"Name set to {name.content}")
        
            try:
                types = await self.bot.wait_for("message", timeout = 30.5, check = check)
            except asyncio.TimeoutError:
                await ctx.send("Timeout")

            else:
                wishwing2.append(str(types.content))
                await ctx.send(f"Type set to {types.content}")

                try:
                    attack = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing2.append(int(attack.content))
                    await ctx.send(f"Attack set to {attack.content}")
                
                try:
                    magic = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing2.append(int(magic.content))
                    await ctx.send(f"Magic set to {magic.content}")
                
                try:
                    defense = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing2.append(int(defense.content))
                    await ctx.send(f"Defense set to {defense.content}")
                
                try:
                    health = await self.bot.wait_for("message", timeout = 30.5, check = check)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout")
                
                else:
                    wishwing2.append(int(health.content))
                    await ctx.send(f"Health set to {health.content}")
                

        


class battle(Cog):
    def __init__(self, bot):
        self.bot = bot
    
       
    @Cog.listener()
    async def on_ready(self):
        print("Battle cog ready!")

   
    @command(name = "battle")    

    #setting up the fight

    async def fight(self, ctx):

        #allow 2 Wishwings to fight each other.

        #Fight info
        await ctx.send("Wishwing Battle")
        await ctx.send(wishwing1[0])
        await ctx.send("TYPE " + wishwing1[1])
        await ctx.send("ATTACK " + str(wishwing1[2]))
        await ctx.send("MAGIC " + str(wishwing1[3]))
        await ctx.send("DEFENSE " + str(wishwing2[4]))
        await ctx.send("VS")
        await ctx.send(wishwing2[0])
        await ctx.send("TYPE " + wishwing2[1])
        await ctx.send("ATTACK " + str(wishwing2[2]))
        await ctx.send("MAGIC " + str(wishwing2[3]))
        await ctx.send("DEFENSE " +  str(wishwing2[4]))
  
        

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

        
        #Fight
        #continue while each Wishwing still has health

        while wishwing1[5] > 0 and wishwing2[5] > 0:
            await ctx.send(f"HEALTH {wishwing1[5]}")
            await ctx.send(f"HEALTH {wishwing2[5]}")

            await ctx.send(f"Go {wishwing1[0]}!")

            for k in enumerate(allignment):
                if wishwing1[1] == wishwing2[1]:
                    string_1_attack = await ctx.send("It did normal damage.")
                    
                
                elif wishwing1[1] == light_weakness and wishwing2[1] == "Light":
                    wishwing1[2] *= 2
                    wishwing1[3] *= 2
                    wishwing1[4] *= 2
                    wishwing2[2] /= 2
                    wishwing2[3] /= 2
                    wishwing2[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    

                elif wishwing1[1] == dark_weakness and wishwing2[1] == "Dark":
                    wishwing1[2] *= 2
                    wishwing1[3] *= 2
                    wishwing1[4] *= 2
                    wishwing2[2] /= 2
                    wishwing2[3] /= 2
                    wishwing2[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                
                
                elif wishwing1[1] == wind_weakness and wishwing2[1] == "Wind":
                    wishwing1[2] *= 2
                    wishwing1[3] *= 2
                    wishwing1[4] *= 2
                    wishwing2[2] /= 2
                    wishwing2[3] /= 2
                    wishwing2[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
            
                elif wishwing1[1] == ice_weakness and wishwing2[1] == "Ice":
                    wishwing1[2] *= 2
                    wishwing1[3] *= 2
                    wishwing1[4] *= 2
                    wishwing2[2] /= 2
                    wishwing2[3] /= 2
                    wishwing2[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                

                elif wishwing1[1] == earth_weakness and wishwing2[1] == "Earth":
                    wishwing1[2] *= 2
                    wishwing1[3] *= 2
                    wishwing1[4] *= 2
                    wishwing2[2] /= 2
                    wishwing2[3] /= 2
                    wishwing2[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                
                
                elif wishwing1[1] == steel_weakness and wishwing2[1] == "Steel":
                    wishwing1[2] *= 2
                    wishwing1[3] *= 2
                    wishwing1[4] *= 2
                    wishwing2[2] /= 2
                    wishwing2[3] /= 2
                    wishwing2[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                
                
                elif wishwing1[1] == fire_weakness and wishwing2[1] == "Fire":
                    wishwing1[2] *= 2
                    wishwing1[3] *= 2
                    wishwing1[4] *= 2
                    wishwing2[2] /= 2
                    wishwing2[3] /= 2
                    wishwing2[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                

            #determine damage
            wishwing2[5] -= (wishwing1[2] + wishwing1[3] - (wishwing2[4] * .5))
            #check to see if wishwing2 can still battle

            if wishwing2[5] <= 0:
                await ctx.send(f"HEALTH {wishwing1[5]}")
                await ctx.send(f"HEALTH 0")
                await ctx.send(f"....{wishwing2[0]} cannot battle anymore!") 
                break

            #Wishwing 2 turn

            await ctx.send(f"HEALTH {wishwing1[5]}")
            await ctx.send(f"HEALTH {wishwing2[5]}")

            await ctx.send(f"Go {wishwing2[0]}!")

            for k in enumerate(allignment):
                if wishwing2[1] == wishwing1[1]:
                    string_1_attack = await ctx.send("It did normal damage.")
                    
                
                elif wishwing2[1] == light_weakness and wishwing1[1] == "Light":
                    wishwing2[2] *= 2
                    wishwing2[3] *= 2
                    wishwing2[4] *= 2
                    wishwing1[2] /= 2
                    wishwing1[3] /= 2
                    wishwing1[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    

                elif wishwing2[1] == dark_weakness and wishwing1[1] == "Dark":
                    wishwing2[2] *= 2
                    wishwing2[3] *= 2
                    wishwing2[4] *= 2
                    wishwing1[2] /= 2
                    wishwing1[3] /= 2
                    wishwing1[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                
                
                elif wishwing2[1] == wind_weakness and wishwing1[1] == "Wind":
                    wishwing2[2] *= 2
                    wishwing2[3] *= 2
                    wishwing2[4] *= 2
                    wishwing1[2] /= 2
                    wishwing1[3] /= 2
                    wishwing1[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
            
                elif wishwing2[1] == ice_weakness and wishwing1[1] == "Ice":
                    wishwing2[2] *= 2
                    wishwing2[3] *= 2
                    wishwing2[4] *= 2
                    wishwing1[2] /= 2
                    wishwing1[3] /= 2
                    wishwing1[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                

                elif wishwing2[1] == earth_weakness and wishwing1[1] == "Earth":
                    wishwing2[2] *= 2
                    wishwing2[3] *= 2
                    wishwing2[4] *= 2
                    wishwing1[2] /= 2
                    wishwing1[3] /= 2
                    wishwing1[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                
                
                elif wishwing2[1] == steel_weakness and wishwing1[1] == "Steel":
                    wishwing2[2] *= 2
                    wishwing2[3] *= 2
                    wishwing2[4] *= 2
                    wishwing1[2] /= 2
                    wishwing1[3] /= 2
                    wishwing1[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                    
                
                
                elif wishwing2[1] == fire_weakness and wishwing1[1] == "Fire":
                    wishwing2[2] *= 2
                    wishwing2[3] *= 2
                    wishwing2[4] *= 2
                    wishwing1[2] /= 2
                    wishwing1[3] /= 2
                    wishwing1[4]/= 2
                    string_1_attack = await ctx.send("It's very effective!")
                

            #determine damage
            wishwing1[5] -= (wishwing2[2] + wishwing2[3] - (wishwing2[4] * .5))   

            #check to see if self can still battle
            if wishwing1[5] <= 0:
                await ctx.send(f"HEALTH 0")
                await ctx.send(f"HEALTH {wishwing2[5]}")
                await ctx.send(f".... {wishwing1[0]} cannot battle anymore!") 
                break

   


def setup(bot):
    bot.add_cog(battle(bot))
    bot.add_cog(stats(bot))
        


        