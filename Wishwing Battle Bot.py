from discord.ext.commands.core import command
import asyncio
import numpy as np
import sys
import discord
from discord.ext import commands


#create class

    class Wishwing:


        async def __init__(self, name, types, STATS, health="===================="):
        #save variables as attributes
            self.name = name
            self.types = types
            self.attack = STATS["Attack"]
            self.magic = STATS["Magic"]
            self.defense = STATS["Defense"]
            self.health = health
            self.bars = 20 #amount of health bars

    #setting up the fight

        async def fight(self, Wishwing2):
        #allow 2 Wishwings to fight each other.

        #Fight info
            print("Wishwing Battle")
            print(self.name)
            print("\nTYPE/", self.types)
            print("\nATTACK/", self.attack)
            print("\nMAGIC/", self.magic)
            print("\nDEFENSE/", self.defense)
            print("\nLEVEL/", 2 * (1 + np.mean([self.attack, self.magic, self.defense])))
            print("\nVS")
            print(Wishwing2.name)
            print("\nTYPE/", Wishwing2.types)
            print("\nATTACK/", Wishwing2.attack)
            print("\nMAGIC/", Wishwing2.magic)
            print("\nDEFENSE/", Wishwing2.defense)
            print("\nLEVEL/", 2 * (1 + np.mean([Wishwing2.attack, Wishwing2.magic, Wishwing2.defense])))

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


            for i,k in enumerate(allignment):
                if self.types == k:
                    string_1_attack = "/nIt did normal damage."
                    string_2_attack = "/nIt did normal damage."
            
                if self.types == light_weakness and Wishwing2.types == "Light":
                    self.attack *= 2
                    self.defense *= 2
                    Wishwing2.attack /= 2
                    Wishwing2.defense /= 2
                    string_1_attack = "/nIt's very effective!"
                    string_2_attack = "/nIt's not very effective...."

                if self.types == dark_weakness and Wishwing2.types == "Dark":
                    self.attack *= 2
                    self.defense *= 2
                    Wishwing2.attack /= 2
                    Wishwing2.defense /= 2
                    string_1_attack = "/nIt's very effective!"
                    string_2_attack = "/nIt's not very effective...."
            
                if self.types == wind_weakness and Wishwing2.types == "Wind":
                    self.attack *= 2
                    self.defense *= 2
                    Wishwing2.attack /= 2
                    Wishwing2.defense /= 2
                    string_1_attack = "/nIt's very effective!"
                    string_2_attack = "/nIt's not very effective...."
            
                if self.types == ice_weakness and Wishwing2.types == "Ice":
                    self.attack *= 2
                    self.defense *= 2
                    Wishwing2.attack /= 2
                    Wishwing2.defense /= 2
                    string_1_attack = "/nIt's very effective!"
                    string_2_attack = "/nIt's not very effective...."

                if self.types == earth_weakness and Wishwing2.types == "Earth":
                    self.attack *= 2
                    self.defense *= 2
                    Wishwing2.attack /= 2
                    Wishwing2.defense /= 2
                    string_1_attack = "/nIt's very effective!"
                    string_2_attack = "/nIt's not very effective...."
            
                if self.types == steel_weakness and Wishwing2.types == "Steel":
                    self.attack *= 2
                    self.defense *= 2
                    Wishwing2.attack /= 2
                    Wishwing2.defense /= 2
                    string_1_attack = "/nIt's very effective!"
                    string_2_attack = "/nIt's not very effective...."
            
                if self.types == fire_weakness and Wishwing2.types == "Fire":
                    self.attack *= 2
                    self.defense *= 2
                    Wishwing2.attack /= 2
                    Wishwing2.defense /= 2
                    string_1_attack = "/nIt's very effective!"
                    string_2_attack = "/nIt's not very effective...."





            
        
        #Fight
        #continue while each Wishwing still has health

            while (self.bars > 0) and (Wishwing2.bars > 0):
                print(f"{self.health}\t\tHEALTH\t{self.health}")
                print(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")

                print(f"Go {self.name}!")

                #determine damage
                Wishwing2.bars -= (self.attack + self.magic)
                Wishwing2.health = ""

                #add back bars plus defense boost
                for j in range(int(Wishwing2.bars + .1 * Wishwing2.defense)):
                    Wishwing2.health = "="
                    print(f"{self.health}\t\tHEALTH\t{self.health}")
                    print(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")   

                #check to see if Wishwing2 can still battle
                if Wishwing2.bars <= 0:
                    print("...." + Wishwing2.name + " cannot battle anymore!") 
                    break

                #Wishwing 2 turn

                print(f"{self.health}\t\tHEALTH\t{self.health}")
                print(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")

                print(f"Go {Wishwing2.name}!")

                #determine damage
                self.bars -= (Wishwing2.attack + Wishwing2.magic)
                self.health = ""

                #add back bars plus defense boost
                for j in range(int(self.bars + .1 * self.defense)):
                    self.health = "="
                    print(f"{self.health}\t\tHEALTH\t{self.health}")
                    print(f"{Wishwing2.health}\t\tHEALTH\t{Wishwing2.health}\n")   

                #check to see if self can still battle
                if self.bars <= 0:
                    print("...." + self.name + " cannot battle anymore!") 
                    break


    client.run("TOKEN")