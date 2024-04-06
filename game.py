import discord
from discord.ext import commands
import configure
intents=discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

know=False

@bot.tree.command()
async def start_game(inter: discord.Interaction):
   # file = discord.File("download.jpg", filename="download.jpg")
    embed=discord.Embed(title="Welcome to this adventure game!",description="In this game you are a famous adventurer .You stumbled upon a village named 'Quazawaaka' near a forest. The villagers tell you about how people keep disappearing in this forest. The forest is vital for daily activties, and hence the people of Quazawaaka ask you for your help.\n`Remember you need to find 3 objects which will help you in your journey.`\n\n Type !start to start the adventure!!",colour=discord.Color.gold())
   # embed.set_image(url="attachment://download.jpg")
  #  embed.set_thumbnail(url="attachment://download.jpg")
  #  embed.set_image(url=configexperiment.Url)
    await inter.response.defer(thinking=True)
    await inter.followup.send(embed=embed)

@bot.command()
async def start(ctx):

    await ctx.send("You venture into the dark forest encounter a fork in the path. On one side you can see an abandoned house, on the other side you can hear roar of a waterfall.")
    await ctx.send("Which way do you go?")
    await ctx.send("(Type !go_to_house or !go_to_waterfall)")

@bot.command()
async def go_to_waterfall(ctx):

    await ctx.send("You have reached the waterfall. Behind the wall of flowing water, slightly obscured by mist is a cave.")
    await ctx.send("Do you choose to go and explore the cave or continue your journey into the forest?")
    await ctx.send("(Type !continue_in_forest or !go_to_cave)")

@bot.command()
async def go_to_cave(ctx):

    await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as a huge monster appears. You then realise that this monster is the reason that the villagers of Quazawaaka have disappeared.")
    await ctx.send("Do you escape into the forest or fight the monster?")
    await ctx.send("(Type !escape_to_forest or !fight_monster)")

@bot.command()
async def fight_monster(ctx):
    
    await ctx.send("You run and attack the monster just to realise that you don't have the right weapons to fight the monster.")
    await ctx.send("The monster grabs you, breaks you in half and gobbles you up.You died :(.")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n The End. \n \n You can play the game again by typing !start.")

@bot.command()
async def esacape_to_forest(ctx):
    know=True
    await ctx.send("As you escape and continue your journey in the the forest you see a person drowning in a turbulent river. As they drown you notice that close to them a sword is sinking. You realise that the sword is specially designed to kill anything and would be very useful to you.")
    await ctx.send("You have time to either save the person or take the sword. What do you do?")
    await ctx.send("(Type !save_person or !take_sword)")

@bot.command()
async def continue_in_forest(ctx):

    await ctx.send("As you continue your journey in the the forest you see a person drowning in a turbulent river. As they drown you notice that close to them a sword is sinking. You realise that the sword is specially designed to kill anything and would be very useful to you.")
    await ctx.send("You have time to either save the person or take the sword. What do you do?")
    await ctx.send("(Type !save_person or !take_sword)")

@bot.command()
async def take_sword(ctx):
    
    await ctx.send("You take the sword and continue walking. You feel a prickling feeling in the back of you neck, as if someone is watching you. 'Who is there ?' you yell. A slender, ethereal figure comess from the shadows. You recognise her as one of the spirits of the forest. You ask the forest spirit if she can help you. She looks furious as she says,'Why should I help you when you let my friend drown?'. She then disappears. You sigh and continue walking.")
    await ctx.send("You then hear the waterfall again. Do you go to the waterfall or continue further into the forest?")
    await ctx.send("Which way do you go? (Type !waterfall_again or !further_into_forest)")

@bot.command()
async def waterfall_again(ctx):
    
    await ctx.send("You have reached the waterfall again.")
    await ctx.send("Do you choose to go and explore the cave behind the waterfall or continue your journey into the forest?")
    await ctx.send("(Type !further_into_forest or !go_to_cave)")

@bot.command()
async def further_into_forest(ctx):
    
    await ctx.send("You continue walking further into the forest.You walk for many hours before you notice that you are walking in circles.")
    await ctx.send("You realise that you are lost. With no way to go anywhere, even back to Quazawaaka, you wander around the forest for days until you finally collapse and die :( .) ")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n The End. \n \n You can play the game again by typing !start.")

@bot.command()
async def save_person(ctx):

    await ctx.send("You manage to save the person just in time. The person thanks you profusely. From the shadows nearby a slender, ethereal figure appears. A forest spirit, you recognise. She thanks you for saving her friend and as a reward gives you a large coin with a map engraved on it. 'This will take you to what you require in your journey', she says and disappears with her friend.")
    await ctx.send("You start following the map on the coin until you reach a mysterious shop in the middle of nowhere. Do you enter the shop or continue following the map? ")
    await ctx.send("(Type !enter_shop or !follow_map)")

@bot.command()
async def follow_map(ctx):

    await ctx.send("You walk for a long time before you reach a field of huge tulip like flowers. In the middle of the field you can see a necklace on a pedestal. A stone carving nearby proclaims that the necklace heals its wearer of any life-threatening injuries.")
    await ctx.send("You remember what the forest spirit said and decide that the necklace would be useful for the journey. Will you enter the field or go further into the forest?")
    await ctx.send("(Type !enter_field or !further_into_forest)")

@bot.command()
async def enter_field(ctx):

    await ctx.send("You enter the field just for the plants to start moving and strangle you. They choke you until you die. :( )")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n The End. \n \n You can play the game again by typing !start.")

@bot.command()
async def enter_shop(ctx):

    await ctx.send("The door creaks as you enter the shop. The place is dusty and quiet. On a window there is an old paper stuck which says that to take anything from the shop something has to be exchanged in return. You browse through the items till you notice that the sword that had sunk into the river is present here.")
    await ctx.send("You realise that you can exchange the coin for the sword or try to steal it as you are sure that you will require the sword in your journey. What will you do?")
    await ctx.send("(Type !exchange_coin or !steal_sword)")

@bot.command()
async def steal_sword(ctx):

    await ctx.send("When you try to steal the sword, you start feeling very dizzy. You manage to take the sword just to collapse right outside the door of the shop. The shop said something has to be exchanged. In your last moments you realise that by stealing you have essentially exchanged you soul, then you die. :( )")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n The End. \n \n You can play the game again by typing !start.")

@bot.command()
async def exchange_coin(ctx):

    await ctx.send("You quickly memorize the map and exchange the coin. You take the sword, exit the shop and follow the map until you reach a field of huge tulip like flowers. In the middle of the field you can see a necklace on a pedestal. A stone carving nearby proclaims that the necklace heals its wearer of any life-threatening injuries.")
    await ctx.send("You remember what the forest spirit said and decide that the necklace would be useful for the journey. Will you go into the field or go further into the forest?")
    await ctx.send("(Type !go_into_field or !further_into_forest)")

@bot.command()
async def go_into_field(ctx):

    await ctx.send("You enter the field just for the plants to start moving and strangle you. You cut down the plants with your sword and manage to go and grab the neckalce. You wear the necklace and it heals you. You continue walking in the forest until you hear the water fall again.")
    await ctx.send("Will you go to the waterfall or go further into the forest?")
    await ctx.send("(Type !go_to_waterfall_again or !further_into_forest)")

@bot.command()
async def go_to_waterfall_again(ctx):
    
    await ctx.send("You have reached the waterfall again.")
    await ctx.send("Do you choose to go and explore the cave behind the waterfall or continue your journey into the forest?")
    await ctx.send("(Type !further_into_forest or !go_into_cave)")

@bot.command()
async def go_into_cave(ctx):
    if know==False:
        await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as a huge monster appears. You then realise that this monster is the reason that the villagers of Quazawaaka have disappeared.")
    else:
        await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as the monster appears.")
    await ctx.send("Do you escape into the forest or fight the monster?")
    await ctx.send("(Type !further_into_forest or !fight_the_monster)")

@bot.command()
async def fight_the_monster(ctx):

    await ctx.send("You run and attack the monster. As it grabs you, you stab the monster's face. It screams and slams you onto a rock. The necklace heals any any damage to your body and you stab the monster's heart and finally the monster dies.")
    await ctx.send("You return to Quazawaaka and announce to the villagers that they are safe now. The villagers thank you and as a show of gratitude, give you enough money to celebrate for a week.")
    await ctx.send("The villagers of Quazawaaka live happily ever after. They gather around every year on this day to tell the tale of a valiant adventurer who saved them from doom  \n The End. \n \n You can play the game again by typing !start.")

@bot.command()
async def go_to_house(ctx):
    
    await ctx.send("After entering the house you see a sphinx standing there, watching you. It comes closer to you and declares that you have to answer its riddles, otherwise it will kill you")
    await ctx.send("You know that you cannot escape it so you have to answer its riddles.")
    await ctx.send("(Type !riddle1 for the 1st one)")

@bot.command()
async def riddle1(ctx):
    #timer needed
    await ctx.send("I'm a guide without a voice, showing paths both near and far,\nI'm filled with lines and symbols, showing places high and low,\nYou'll need me on an adventure, whether by foot, plane, or car.\nWith me, you'll never lose your way, no matter where you go.\nAm I a compass, a map, a chart or a star?\n")
    await ctx.send("(Type !compass or !map or `!)")





bot.run(configure.DISCORD_TOKEN)