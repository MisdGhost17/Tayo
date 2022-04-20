import discord
from discord.ext import commands
from index import token

client = commands.Bot(command_prefix='/')

emb = discord.Embed


@client.event
async def on_ready():
    print("Let's go")

@client.command()
async def info(message):
    author = message.author
    emb = discord.Embed(title=author.name + ' info')
    emb.add_field(name='Id:', value=author.id, inline=False)
    emb.add_field(name='Account at:', value=author.created_at, inline=False)
    emb.add_field(name='Joined at:', value=author.joined_at, inline=False)
    emb.add_field(name='Guild:', value=author.guild, inline=False)
    for role in author.roles:
        emb.add_field(name='Guild specific:', value=role, inline=False)
    emb.add_field(name='Bot:', value=author.bot, inline=False)
    emb.set_image(url=author.avatar_url)
    emb.add_field(name='Avatar url:', value=author.avatar_url, inline=False)
    emb.set_footer(text=author.name, icon_url=author.avatar_url)
    await message.channel.send(embed=emb)

client.run(token)
