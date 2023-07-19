import discord
from discord.ext import commands
import random
import datetime
import pytz

BOT_TOKEN = "MTEyOTU1MTcyOTI5MDEyNTMzMg.G9dwso" \
            ".Z7HfUrS8cYaJnpzk_7oBF06OucPzIxZjtyunxg"
USER_ID = 1129551729290125332

# Champchas Channel:
CHANNEL_ID = 1062156146628120606
# Test Channel:
# CHANNEL_ID = 1129596258957410325

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    with open("log.txt", 'r') as f:
        line = f.readline().strip()
    if line == "false":
        await channel.send(
            'Im online bro how do you do bro \U0001F60F\U0001F60F')
        with open("log.txt", 'w') as f:
            f.write("true")

    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(
                                  type=discord.ActivityType.watching,
                                  name="you like a Pekachu", ))
    print("Bot is online!")

    messages = [message async for message in channel.history(limit=50) if
                message.author.id != USER_ID and "!" not in message.content]
    for message in messages:
        if message.content.lower == "ufff" and message.author.id == 294574770006130689:
            await message.add_reaction("\U0001f92a")


@bot.event
async def on_message(message):
    print(f"MESSAGE in {message.channel} -- {message.author} : {message.content}")

    if message.author.id == USER_ID:
        return

    if "!" in message.content:
        for command in bot.commands:
            if message.content == "!" + command.name:
                await message.add_reaction("\N{WHITE HEAVY CHECK MARK}")
        await bot.process_commands(message)

        return
    if random.random() <= .0001:
        await message.add_reaction("\U0001f618\U0001f48B")
        print("Reacted with a kiss!")
    elif random.random() <= .005:
        await message.add_reaction("\U0001f4e0")
        print("Reacted with a fax!")
    elif random.random() <= .025:
        don_emoji = bot.get_emoji(948093363930951720)
        smirk_emoji = '\U0001F60F'
        await message.add_reaction(don_emoji)
        await message.add_reaction(smirk_emoji)
        print("Reacted with a smirk!")


@bot.command()
async def doof(ctx):
    channel = ctx.channel

    messages = [message async for message in channel.history(limit=50) if
                message.author.id != USER_ID and "!" not in message.content]
    msg = random.choice(messages)
    await msg.reply(file=discord.File('doofus.jpg'))
    print("Sent a doofus!")


@bot.event
async def on_message_delete(message):
    channel = message.channel
    async for entry in message.guild.audit_logs(limit=1,
                                                action=discord.
                                                AuditLogAction.
                                                message_delete):

        time_rn = datetime.datetime.now(pytz.timezone('UTC'))
        audit_time = entry.created_at

        same_time = False
        if audit_time.year == time_rn.year:
            if audit_time.month == time_rn.month:
                if audit_time.day == time_rn.day:
                    if audit_time.hour == time_rn.hour:
                        if audit_time.minute == time_rn.minute:
                            if abs(audit_time.second - time_rn.second) < 2:
                                same_time = True

        if same_time:
            await channel.send(f"Ooohh {entry.user.mention} deleted **\""
                               f"{message.content}\"** by "
                               f"{message.author.mention}!")
            print("Snitched on a deleted message!")

    # If message was deleted by sender:
    # if not same_time:
    #     await channel.send(f"Ooohh {message.author.mention} deleted **\""
    #                        f"{message.content}\"** (which he sent)")
    #     print("Snitched on a deleted message!")
    # Try with embeds in future?


@bot.command()
async def m8b(ctx, *, question=""):
    yes_responses = ["It is certain.", "It is decidedly so.", "Without a doubt",
                 "Yes definitely.", "You may rely on it.",
                 "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                 "Signs point to yes.",
                 "NEESH SAYS YES!"]
    neutral_responses = ["Reply hazy, try again.",
                 "Ask again later.", "Better not tell you now.",
                 "Cannot predict now.", "Concentrate and ask again."]
    no_responses = ["Don't count on it.", "My reply is no.", "My sources say no.",
                 "Outlook not so good.", "Very doubtful.",  "NEESH SAYS NO!"]

    if question == "":
        await ctx.reply("Bro put something in plz")
        return
    if "stay" in question:
        response = random.choice(yes_responses + neutral_responses)
    elif "leave" in question:
        response = random.choice(no_responses + neutral_responses)
    else:
        response = random.choice(yes_responses + no_responses + neutral_responses)
    await ctx.reply(
        f"\U0001F3B1 Here's your answer dyude: **{response}**")
    print("Used a magic 8 ball!")


@bot.command()
async def quote(ctx):
    with open("neesh_quotes.txt", 'r') as quote_file:
        lines = quote_file.readlines()
    await ctx.send(random.choice(lines))
    print("Told a Neesh Quote!")


bot.run(BOT_TOKEN)
