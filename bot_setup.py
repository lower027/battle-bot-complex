from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.enums import Status
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from glob import glob
from pathlib import Path

prefix = "!"
owner = 828499906661449739
server_id = 874471254118248488
channel_id = 874471254118248491
cogs = [p.stem for p in Path(".").glob("./cogs/*.py")]

class Bot(BotBase):
    def __init__(self):
        self.prefix = prefix
        self.ready = False
        self.guild = None
        self.schedueler = AsyncIOScheduler()
        self.wishwings = {}

        super().__init__(command_prefix = prefix, owner_id = owner)

    def setup(self):
        for cog in cogs:
            self.load_extension(f"cogs.{cog}")
            print("Cogs loaded!")
        print("Setup complete!")
        


    def run(self, version):
        self.version = version

        print("Running setup...")
        self.setup()

        with open("./token.txt") as tokenfile:
            self.token = tokenfile.read()

        print("Running bot...")
        super().run(self.token, reconnect = True)


    async def on_connect(self):
        print("Bot connected!")
    
    async def on_disconnect(self):
        print("Bot disconnected!")
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(server_id)
            print("Bot ready.")

            channel = self.get_channel(channel_id)
            await channel.send("Bot online!")
        
        else:
            print("Bot reconnected.")

            channel = self.get_channel(channel_id)
            await channel.send("Bot offline!")
        
        async def on_message(self, message):
            if not message.author.bot:
               await self.process_commands(message)

    
bot = Bot()
