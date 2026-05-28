import discord
from discord.ext import commands
import random
from datetime import timedelta
import statistics
import operator
import secrets
import string

intents = discord.Intents.default()
intents.message_content = True

# Här sätter vi prefixet till komma (,)
bot = commands.Bot(command_prefix='?', intents=intents)

def jokes_not_command(joke_number):
    jokes_list = [
        "Why don't skeletons fight eachother?\n\nBecause they don't have the guts",
        "I used to play piano by ear…\n\nNow I use my hands",
        "Why did the math book look sad?\n\nBecause it had too many problems",
        "What do you call cheese that isn’t yours?\n\nNacho cheese",
        "Did you hear about the restaurant on the moon?\n\nGreat food, no atmosphere"
    ]
    return jokes_list[joke_number - 1]

listlist = [
    '?help - visar kommandona', 
    '?introduction - botens introduktion' ,
    '?roll - rullar ett nummer mellan talen du valt, samt under 20 om du valt bara ett nummer',
    '?jokes - genererar ett av 5 olika skämt',
    '?ping - pingar boten',
    '?timeout - timeouta en person eller bot',
    '?kick - sparka en person eller bot',
    '?ban - banna en person eller bot',
    '?turn - vänder om meningen du skriver efter. Ex: ?turn godmorgon',
    '?count - räknar talen du anget. Ex: ?count 20 + 10, ?count 30 / 20', 
    '?statistic - ger medelvärde, median och typvärde av talen som anges. Ex: ?statistic 10 10 40 40 20', 
    '?caesar - krypterar meningen du angett efter du anger hur mycket du vill flytta meningen med. Ex: ?caesar 5 abc',
    '?palindrom - kollar om ordet är en palindrom',
    '?password - boten skapar ett 12 långt lösenord'
]

@bot.event
async def on_ready():
    print(f'Inloggad som {bot.user}')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

bot.remove_command("help")  #tar bort hjälp kommandot
@bot.command()  #lägger till det nya hjälp kommandot
async def help(ctx):
    await ctx.send("\n".join(listlist)) #slår ihop listan till en string, .send() kan inte skicka listor annars

@bot.command()  #introduktion
async def introduction(ctx):
    await ctx.send('Jag är emo svampbob')

@bot.command()  #rullar ett nummer
async def roll(ctx, max_number: int = 20):
    if max_number > 1000:
        await ctx.channel.send(f"Enter a valid number below 1000")
    else:
        random_number = random.randint(1, max_number)
        await ctx.channel.send(f"You rolled {random_number}! (1 - {max_number})")

@bot.command()  #returnerar ett av 5 dåliga skämt
async def jokes(ctx):
    joke_number = random.randint(1,5)
    await ctx.send(jokes_not_command(joke_number))  #fungerar, men inte bra

@bot.command()  #pingar botten och anger dess latency (ping)
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

#första lektionen ovan, resten var under naturen

@bot.command()  #timeouta medlemmar
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, minutes: int):
    await member.timeout(timedelta(minutes=minutes))
    await ctx.send(f"Bye Bye for now {member}")

@bot.command()  #sparka medlemmar
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):    #VERY IMPORTANT YOU NEED TO CAPITALIZE THE Member
    await member.kick(reason=reason)                            #kicks a person
    await ctx.send(f"Bye Bye now {member}")

@bot.command()  #banna medlemmar
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None): #osäker varför man behöver *, also bans a person
    await member.ban(reason=reason)
    await ctx.send(f"Bye Bye for real now {member}")

#andra lektionen nedan

@bot.command()  #reverse text
async def turn(ctx, text : str):
    reversed_text = ''
    for char in text:
        reversed_text = char + reversed_text
    await ctx.send(reversed_text)

@bot.command()  #mattematik
async def count(ctx, number_1, op, number_2):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow  #to the power of
    }

    try: 
        number_1 = float(number_1)
        number_2 = float(number_2)

        if op not in ops:
            await ctx.send("Ange en riktig operator")
            return

        result = ops[op](number_1, number_2)
        result_rounded_off = round(result) #avrundar nedåt

        await ctx.send(f'Det blir {result} och avrundat {result_rounded_off}')

    except ValueError:
        await ctx.send("Stop")
    except ZeroDivisionError:
        await ctx.send("Du kan inte dividera med noll")
    

@bot.command()  #statestik
async def statistic(ctx, *numbers : int):   #bs vadå *numbers 
    if not int:
        await ctx.send('Enter valid integers')
    else:
        medel = sum(numbers) / len(numbers)
        median = statistics.median(numbers)         #allat thinking for a one liner, ggs 5 times
        type_value = statistics.mode(numbers)       #samma här, statistics my hero
        await ctx.send(f'Medelvärdet är {medel} \n Medianen är {median} \n Typvärdet är {type_value}')

@bot.command()  #caesar kryptering
async def caesar(ctx, move_number : int, sentence : str):
    results = ''    #koden nedan är tagen och omvandlad av mig från en av mina förra uppgifter

    for i in sentence:
        if i.islower():
            start = ord("a")
        else:
            start = ord("A")

        position = ord(i) - start
        new_position = (position + move_number) % 26
        new_sentence = chr(new_position + start)
        results += new_sentence
    await ctx.send(results)

#tredje lektionen nedan

@bot.command()
async def palindrom(ctx, text):
    palindrom_check = ''
    for char in text:
        palindrom_check = char + palindrom_check
    if palindrom_check == text:
        await ctx.send("Det är en palindrom")
    else:
        await ctx.send("Det är inte en palindrom")

@bot.command()
async def password(ctx):
    password_stuff = [] #blev inge glad när man hade de nedan i listan
    password_stuff.append(secrets.choice(string.ascii_lowercase))
    password_stuff.append(secrets.choice(string.ascii_uppercase))
    password_stuff.append(secrets.choice(string.digits))
    password_stuff.append(secrets.choice(string.punctuation))
    
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(length - 4):
        random_characters = secrets.choice(characters)
        password_stuff.append(random_characters)

    secrets.SystemRandom().shuffle(password_stuff)

    random_password = ''
    for char in password_stuff:
        random_password += char

    await ctx.send(random_password)   #alternativt kunde man köra password = secrets.token_urlsafe(12), men det är en one liner

bot.run("")