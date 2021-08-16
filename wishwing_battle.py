import asyncio
from discord.ext.commands.core import check
import numpy as np
import sys
import discord
from discord.ext.commands import command
from discord.ext.commands import Cog
from discord import Embed
import random

wishwing1 = None  # name, type, attack, magic, defense, HP

wishwing2 = None  # name, type, attack, magic, defense, HP




class WishWing:
    def __init__(self, name, w_type, attack, magic, defense, speed, hp):
        self.name = name
        self.type = all_types[w_type]
        self.attack = int(attack)
        self.magic = int(magic)
        self.defense = int(defense)
        self.speed = int(speed)
        self.hp = int(hp)

    def __repr__(self):
        return f"WishWing: name={self.name}, type={self.type}, attack={self.attack}, magic={self.magic}, defense={self.defense}, speed = {self.speed}, hp={self.hp}"
    



        


class stats(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Stats cog ready!")

    @command(name="input")
    async def stat_input(self, ctx):
        global wishwing1, wishwing2
        waiting_wishwing_1 = Embed(title = "Waiting for stats for Wishwing 1...", description = "Enter: Name, type, attack, magic, defense, speed, HP.")
        await ctx.send(embed = waiting_wishwing_1)

        def check(message: discord.Message) -> bool:
            return message.author == ctx.author

        """WishWing1!!!"""
        try:
            name = await self.bot.wait_for("message", timeout=30.5, check=check)
            types = await self.bot.wait_for("message", timeout=30.5, check=check)
            attack = await self.bot.wait_for("message", timeout=30.5, check=check)
            magic = await self.bot.wait_for("message", timeout=30.5, check=check)
            defense = await self.bot.wait_for("message", timeout=30.5, check=check)
            speed = await self.bot.wait_for("message", timeout = 35.5, check=check)
            health = await self.bot.wait_for("message", timeout=30.5, check=check)          
             
        except asyncio.TimeoutError:
            timeout = Embed(title = "Timeout", description = "You didn't send a response in time...")
            await ctx.send(embed = timeout)
        
        

        else:
            wishwing1 = WishWing(str(name.content), str(types.content), str(attack.content), str(magic.content), str(defense.content), str(speed.content), str(health.content))
            wishwing1_stats = Embed(title = f"{wishwing1.name}", description = f"{wishwing1}")
            await ctx.send(embed = wishwing1_stats)

        """WishWing2!!!"""
        waiting_wishwing_2 = Embed(title = "Waiting for stats for Wishwing 2...", description = "Enter: Name, type, attack, magic, defense, speed, HP")
        await ctx.send(embed = waiting_wishwing_2)

        try:
            name = await self.bot.wait_for("message", timeout=30.5, check=check)
            types = await self.bot.wait_for("message", timeout=30.5, check=check)
            attack = await self.bot.wait_for("message", timeout=30.5, check=check)
            magic = await self.bot.wait_for("message", timeout=30.5, check=check)
            defense = await self.bot.wait_for("message", timeout=30.5, check=check)
            speed = await self.bot.wait_for("message", timeout=30.5, check=check)
            health = await self.bot.wait_for("message", timeout=30.5, check=check)
        except asyncio.TimeoutError:
            timeout = Embed(title = "Timeout", description = "You didn't send a response in time...")
            await ctx.send(embed = timeout)


        else:
            wishwing2 = WishWing(str(name.content), str(types.content), str(attack.content), str(magic.content), str(defense.content), str(speed.content), str(health.content))
            wishwing2_stats = Embed(title = f"{wishwing2.name}", description = f"{wishwing2}")
            await ctx.send(embed = wishwing2_stats)
           

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

    def __lt__(self, other):
        if other in self.strong:
            return False
        if other in self.weak:
            return True

    def __eq__(self, other):
        if other not in self.strong + self.weak:
            return True
        else:
            return False
    


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
        
    #allow 2 Wishwings to fight each other.
        
       #Fight info
        battle_opener = Embed(title = f"""Wishwing battle
        {wishwing1}
        VS.
        {wishwing2}""")

        await ctx.send(embed = battle_opener)

        
        #Fight
        #continue while each Wishwing still has health

        random_attack_lines_1 = [
        f"{wishwing1.name} threw a punch at {wishwing2.name}!",
        f"{wishwing1.name} kicked {wishwing2.name} in the stomach!",
        f"{wishwing2.name} couldn't dodge {wishwing1.name}'s hit!",
        "Pow!",
        f"{wishwing2.name} got sacked in the gut!",
        f"{wishwing1.name} landed a clean hit!",
        "Smack!",
        "Bam!",
        "Flying kickapow!",
        "Locked and loaded, son!",
        "Look at that tornado kick!",
        f"Go {wishwing1.name}!",
        "Ouch! That's gotta hurt!",
        "Slammed 'em!"
        ]

        random_attack_lines_2 = [
        f"{wishwing2.name} threw a punch at {wishwing1.name}!",
        f"{wishwing2.name} kicked {wishwing1.name} in the stomach!",
        f"{wishwing1.name} couldn't dodge {wishwing2.name}'s hit!",
        "Pow!",
        f"{wishwing1.name} got sacked in the gut!",
        f"{wishwing2.name} landed a clean hit!",
        "Smack!",
        "Bam!",
        "Flying kickapow!",
        "Locked and loaded, son!",
        "Look at that tornado kick!",
        f"Go {wishwing2.name}!",
        "Ouch! That's gotta hurt!"
        "Slammed 'em!"
        ]

        health = Embed(title = "Health", description = f"""{wishwing1.name} HEALTH {int(wishwing1.hp)}
{wishwing2.name} HEALTH {int(wishwing2.hp)}""")

        await ctx.send(embed = health)

        while wishwing1.hp> 0 and  wishwing2.hp> 0:

            if wishwing1.speed > wishwing2.speed:

                #wishwing 1 turn

                random_lines_1 = Embed(title = f"{wishwing1.name}'s turn!", description = random.choice(random_attack_lines_1))
                await ctx.send(embed = random_lines_1)  
            

                #determine damage    
                if wishwing1.type > wishwing2.type:
                    wishwing2.hp -= (wishwing1.attack * 2 + wishwing1.magic * 2 - (wishwing2.defense * .25))
                
                elif wishwing1.type < wishwing2.type:
                    wishwing2.hp -= (wishwing1.attack * 0.5 + wishwing1.magic * 0.5 - (wishwing2.defense * 1))
            
                elif wishwing1.type == wishwing2.type:
                    wishwing2.hp -= (wishwing1.attack + wishwing1.magic - (wishwing2.defense * .5))
                
            
            #check to see if wishwing2 can still battle

                if wishwing2.hp <= 0:
                    wishwing2_lost = Embed(title = "Health", description = 
                    f"""{wishwing1.name} HEALTH {int(wishwing1.hp)}
{wishwing2.name} HEALTH 0""")
                    wishwing2_fainted = Embed(title = "Battle log", description = f".... {wishwing2.name} cannot battle anymore!") 
                    await ctx.send(embed = wishwing2_lost)
                    await ctx.send(embed = wishwing2_fainted)
                    break
                
            

                #Wishwing 2 turn

                random_lines_2 = Embed(title = f"{wishwing2.name}'s turn!", description = random.choice(random_attack_lines_2))
                await ctx.send(embed = random_lines_2)


                #determine damage
                    
                if wishwing2.type > wishwing1.type:
                    wishwing1.hp -= (wishwing2.attack * 2 + wishwing2.magic * 2 - (wishwing1.defense * .25))
                    
                elif wishwing2.type < wishwing1.type:
                    wishwing1.hp -= (wishwing2.attack * 0.5 + wishwing2.magic * 0.5 - (wishwing1.defense * 1))
                
                elif wishwing2.type == wishwing1.type:
                    wishwing1.hp -= (wishwing2.attack + wishwing2.magic - (wishwing1.defense * .5))
                

           
            

                
                    
            elif wishwing2.speed > wishwing1.speed:
                #Wishwing 2 turn

                random_lines_2 = Embed(title = f"{wishwing2.name}'s turn!", description = random.choice(random_attack_lines_2))
                await ctx.send(embed = random_lines_2)


                #determine damage
                    
                if wishwing2.type > wishwing1.type:
                    wishwing1.hp -= (wishwing2.attack * 2 + wishwing2.magic * 2 - (wishwing1.defense * .25))
                    
                elif wishwing2.type < wishwing1.type:
                    wishwing1.hp -= (wishwing2.attack * 0.5 + wishwing2.magic * 0.5 - (wishwing1.defense * 1))
                
                elif wishwing2.type == wishwing1.type:
                    wishwing1.hp -= (wishwing2.attack + wishwing2.magic - (wishwing1.defense * .5))
                
                #check to see if Wishwing1 can still battle
                if wishwing1.hp <= 0:
                    wishwing1_lost = Embed(title = "Health", description =  
                    f"""{wishwing1.name} HEALTH 0
    {wishwing2.name} HEALTH {int(wishwing2.hp)}""")
                    wishwing1_fainted = Embed(title = "Battle log", description = f".... {wishwing1.name} cannot battle anymore!") 
                    await ctx.send(embed = wishwing1_lost)
                    await ctx.send(embed = wishwing1_fainted)
                    break

                random_lines_1 = Embed(title = f"{wishwing1.name}'s turn!", description = random.choice(random_attack_lines_1))
                await ctx.send(embed = random_lines_1)  
            

                #determine damage    
                if wishwing1.type > wishwing2.type:
                    wishwing2.hp -= (wishwing1.attack * 2 + wishwing1.magic * 2 - (wishwing2.defense * .25))
                
                elif wishwing1.type < wishwing2.type:
                    wishwing2.hp -= (wishwing1.attack * 0.5 + wishwing1.magic * 0.5 - (wishwing2.defense * 1))
            
                elif wishwing1.type == wishwing2.type:
                    wishwing2.hp -= (wishwing1.attack + wishwing1.magic - (wishwing2.defense * .5))
                
                #check to see if wishwing2 can still battle

                if wishwing2.hp <= 0:
                    wishwing2_lost = Embed(title = "Health", description = 
                    f"""{wishwing1.name} HEALTH {int(wishwing1.hp)}
{wishwing2.name} HEALTH 0""")
                    wishwing2_fainted = Embed(title = "Battle log", description = f".... {wishwing2.name} cannot battle anymore!") 
                    await ctx.send(embed = wishwing2_lost)
                    await ctx.send(embed = wishwing2_fainted)
                    break


            

class instructions(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name = "instructions")

    async def instructions(self, ctx):
        #instructions
        bot_instructions = Embed(title = "Instructions for Battle Bot", 
        description = """Hello! Thank you for using the Wishwing Battle bot!
        
        1. In order to start using the bot, type "!input" to enter your Wishwing's stats.
        2. This is VERY important. Enter the stats in this order: NAME, TYPE, ATTACK, MAGIC, DEFENSE, SPEED, HP
            - You have 30 seconds to enter each stat. If you fail to enter it in that amount of time, it will timeout and you'll have to start over.
        3. Once it's entered for both Wishwings, type "!battle"!
        4. The bot will simulate the battle between two characters until it finishes. At that point, you can start over!

        Fire: weak = ["Earth", "Wind"], strong = ["Ice", "Dark"],
        Light: weak=["Dark", "Ice"], strong=["Dark"],
        Dark: weak=["Light, Fire"], strong = ["Light"],
        Wind: weak = ["Steel", "Ice"], strong = ["Earth", "Fire"],
        Ice: weak = ["Fire", "Steel"], strong = ["Light", "Wind"],
        Earth: weak = ["Ice", "Wind"], strong = ["Steel", "Fire"],
        Steel: weak = ["Fire", "Earth"], strong = ["Wind", "Ice"]"""
        )
        await ctx.send(embed = bot_instructions)

            

   


def setup(bot):
    bot.add_cog(battle(bot))
    bot.add_cog(stats(bot))
    bot.add_cog(instructions(bot))
        


        