# -*- coding: utf-8 -*-

import os
from asyncio import new_event_loop, sleep

from discord import Game, Embed
from discord.ext import commands


token = os.environ['TOKEN']
loop = new_event_loop()

async def run():
    bot = MyBot()
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.logout()

class MyBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("::"), loop=loop, case_insensitive=True)
        self.remove_command('help')
        
    async def on_ready(self):
        print(f"{os.path.basename(__file__)} total_shard:{self.shard_count}")
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
    
    async def on_guild_join(self, _):
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
            
    async def on_guild_remove(self, _):
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
            
if __name__ == '__main__':
    main_task = loop.create_task(run())
    loop.run_until_complete(main_task)
    loop.close()
