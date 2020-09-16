# -*- coding: utf-8 -*-

import os
from asyncio import new_event_loop, sleep

from discord import Game, Embed
from discord.ext import commands


token, prefix = os.environ['TOKEN'], "::"
loop = new_event_loop()

async def run():
    return
    bot = MyBot()
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.logout()

class MyBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(prefix), loop=loop, case_insensitive=True)
        self.remove_command('help')
        try:
            self.load_extension(f"cogs.help")
        except commands.ExtensionAlreadyLoaded:
            pass

    async def on_ready(self):
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
    
    async def on_message(self, message):
        if message.channel.id in [668071116878643212, 721706454935011389, 668071221165817894, 688679140915937293, 694956814927921213, 750656481124417567]:
            return await message.publish()
        
        if message.content == f"{prefix}help":
            await self.process_commands(message)
            
    async def on_guild_join(self, _):
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
            
    async def on_guild_remove(self, _):
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
            
if __name__ == '__main__':
    main_task = loop.create_task(run())
    loop.run_until_complete(main_task)
    loop.close()
