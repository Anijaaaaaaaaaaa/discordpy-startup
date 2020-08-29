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
        
    @bot.command()
    async def help(ctx):
        invite = {"TAOの招待": "https://tukisima.com/invite", "BOT専用-TAOの招待": "https://discordapp.com/api/oauth2/authorize?client_id=695288604829941781&permissions=3533888&scope=bot"}
        web = {"TAOのWEB": "https://tukisima.com", "TAO寄付サイト": "https://taqooto.wixsite.com/tao-donate", "TAO公式Wiki": "https://wiki3.jp/discord_tao"}
        discord = {"公式鯖の招待": "https://discord.gg/d7Qqfhy", "ログ鯖の招待": "https://discord.gg/VHuzWKv", "絵師鯖の招待": "https://discord.gg/qdVsWjE"}
        des = "```現在、諸事情により9月の16日まで使用不可能となっております。\nTAOの今後は公式鯖に入っていればお知らせ随時お知らせ致します。\n下記のURLにTAO関連のURLを張り付けております。```"
        des += ">>> TAO自体の寄付金は止めています。\n諸事情を知って個人的に寄付をしてくださる方は\n<@304932786286886912>のDMまでお願いします；；"
        embed = Embed(title=f"現在TAOは使用できません。", description=des)
        embed.add_field(name=await all_function.kyomu(cur, user_id, "BOT招待:"), value=" | ".join([f"[{t[0]}](<{t[1]}>)" for t in list(invite.items())]), inline=False)
        embed.add_field(name=await all_function.kyomu(cur, user_id, "TAO関連のWEB:"), value=" | ".join([f"[{t[0]}](<{t[1]}>)" for t in list(web.items())]), inline=False)
        embed.add_field(name=await all_function.kyomu(cur, user_id, "TAO関連のDiscord鯖:"), value=" | ".join([f"[{t[0]}](<{t[1]}>)" for t in list(discord.items())]), inline=False)
        embed.set_thumbnail(url=self.user.avatar_url_as())
        msg = await ctx.send(embed=embed)
        await sleep(10)
        await msg.delete()
    
    async def on_guild_join(self, _):
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
            
    async def on_guild_remove(self, _):
        return await self.change_presence(activity=Game(name=f"{prefix}helpのみ使用可能 | {len(self.guilds)}guilds", type=1))
            
if __name__ == '__main__':
    main_task = loop.create_task(run())
    loop.run_until_complete(main_task)
    loop.close()
