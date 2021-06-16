from discord.ext import commands
from config import settings
from random import choice
import wikiquote
import discord

bot = commands.Bot(command_prefix="!")

good_words = [
    "еврей",
    "евреях",
    "Евреях",
    "Семитах",
    "семитах",
    "Иудеях",
    "иудеях",
    "евреи",
    "еврейка",
    "еврейки",
    "Евреи",
    "Еврей",
    "Еврейка",
    "Еврейки",
    "Иудеи",
    "иудеи",
    "семиты",
    "Семиты",
    "семитах",
    "иудеях",
    "еврейках",
    "семитках",
    "иудейках",
]
bad_words = [
    "жидах",
    "Жидах",
    "жиды",
    "жид",
    "жидов",
    "жидах",
    "жидовский",
    "Жид",
    "Жидов",
    "Жиды",
    "Жидовский",
    "жыд",
    "жыдовский",
    "жыды",
    "Жыд",
    "Жыды",
    "Жыдовский",
    "ЖЫДЫ",
]
authors = ["Friedrich Nietzsche", "Sigmund Freud", "Mikhail Bakunin", "Adam Smith", "Friedrich Hayek", "Adolf Hitler", "Aleister Crowley", "H. P. Lovecraft", "Johann Wolfgang von Goethe", "Peter Kropotkin", "Gautama Buddha", "Jesus", "Max Stirner"]


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    for word in good_words:
        if word in message.content:
            await message.channel.send(
                "Слава Израилю! Слава богоизбранному народу! :flag_il:"
            )
            return

    for word in bad_words:
        if word in message.content:
            await message.channel.send(
                "https://en.wikipedia.org/wiki/List_of_Israeli_assassinations"
            )
            return

    await bot.process_commands(message)


@bot.command()
async def quote(ctx):
    author = choice(authors)
    quote = choice(wikiquote.quotes(author))

    embed = discord.Embed(title="Quote", description=f'"{quote}"', color=0x00BFFF)
    embed.set_footer(text=f"© {author}")

    await ctx.send(embed=embed)


bot.run(settings["token"])