import discord
from discord.ext import commands
from index import token


client = discord.Client()
clientuser = discord.ClientUser

emb = discord.Embed


@client.event
async def on_ready():
    print("Let's go")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        emb = discord.Embed(title=message.author.name + ' info')
        emb.add_field(name='Id:', value=message.author.id, inline=False)
        emb.add_field(name='Created at:', value=message.author.created_at, inline=False)
        emb.add_field(name='Joined at:', value=message.author.joined_at, inline=False)
        for role in message.author.roles:
            emb.add_field(name='Roles:', value=role, inline=False)
        emb.add_field(name='Status:', value=message.author.status, inline=False)
        emb.add_field(name='Mobile status:', value=message.author.mobile_status, inline=False)
        emb.add_field(name='Raw status:', value=message.author.raw_status, inline=False)
        emb.add_field(name='Desktop status:', value=message.author.desktop_status, inline=False)
        emb.add_field(name='Web status:', value=message.author.web_status, inline=False)
        emb.set_image(url=message.author.avatar_url)
        emb.add_field(name='Avatar url:\n', value=message.author.avatar_url, inline=False)
        emb.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=emb)

client.run(token)
