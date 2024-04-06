import discord
from discord.ext import commands
import configure
import random
import asyncio

intents=discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

know=False

@bot.tree.command()
async def start_game(inter: discord.Interaction):

    embed=discord.Embed(title="Welcome to this adventure game 🎮!",description="In this game 🎮 you are a famous adventurer 🧙 .You stumbled upon a village named 'Quazawaaka' near a 🌳forest🌳. The villagers tell you about how people keep disappearing in this 🌳forest🌳. The 🌳forest🌳 is vital for daily activties, and hence the people of Quazawaaka ask you for your help.\n`Remember you need to find 3 objects which will help you in your journey.`\n\n Type !start to start the adventure!!",colour=discord.Color.gold())

    await inter.response.defer(thinking=True)
    await inter.followup.send(embed=embed)

@bot.command()
async def start(ctx):
    with open('forest.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You venture into the dark 🌳forest🌳 encounter a fork in the path. On one side you can see an abandoned house, on the other side you can hear roar of a waterfall.")
        await ctx.send("Which way do you go?")
        await ctx.send("(Type `!go_to_house` or `!go_to_waterfall`)")

@bot.command()
async def go_to_waterfall(ctx):
    with open('waterfall.jpg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You have reached the waterfall. Behind the wall of flowing water, slightly obscured by mist is a cave.")
        await ctx.send("Do you choose to go and explore the cave or continue your journey into the 🌳forest🌳?")
        await ctx.send("(Type `!continue_in_forest` or `!go_to_cave`)")

@bot.command()
async def go_to_cave(ctx):
    with open('cave.png', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as a huge monster👺 appears. You then realise that this monster👺 is the reason that the villagers of Quazawaaka have disappeared.")
        await ctx.send("Do you escape into the 🌳forest🌳 or fight the monster👺?")
        await ctx.send("(Type `!escape_to_forest` or `!fight_monster`)")

@bot.command()
async def fight_monster(ctx):
    
    await ctx.send("You run and attack the monster👺 just to realise that you don't have the right weapons to fight the monster👺.")
    await ctx.send("The monster👺 grabs you, breaks you in half and gobbles you up.You died :(.")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def esacape_to_forest(ctx):
    know=True
    with open('Screenshot 2024-04-02 231837.png', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("As you escape and continue your journey in the the 🌳forest🌳 you see a person drowning in a turbulent river. As they drown you notice that close to them a sword🗡️ is sinking. You realise that the sword🗡️ is specially designed to kill anything and would be very useful to you.")
        await ctx.send("You have time to either save the person or take the sword🗡️. What do you do?")
        await ctx.send("(Type `!save_person` or `!take_sword`)")

@bot.command()
async def continue_in_forest(ctx):
    with open('river.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("As you continue your journey in the the 🌳forest🌳 you see a person drowning in a turbulent river. As they drown you notice that close to them a sword🗡️ is sinking. You realise that the sword🗡️ is specially designed to kill anything and would be very useful to you.")
        await ctx.send("You have time to either save the person or take the sword🗡️. What do you do?")
        await ctx.send("(Type `!save_person` or `!take_sword`)")
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and isinstance(message.content, str)
        try:
            await bot.wait_for('message', timeout=8, check=check)

        except asyncio.TimeoutError:
            await ctx.send("You took too long to guess. .")
            await ctx.send("(Type `!further_into_forest` to continue)")

@bot.command()
async def take_sword(ctx):
    
    await ctx.send("You take the sword🗡️ and continue walking. You feel a prickling feeling in the back of you neck, as if someone is watching you. 'Who is there ?' you yell. A slender, ethereal figure comess from the shadows. You recognise her as one of the spirits of the forest 🧝. You ask the forest spirit🧝 if she can help you. She looks furious as she says,'Why should I help you when you let my friend drown?'. She then disappears. You sigh and continue walking.")
    await ctx.send("You then hear the waterfall again. Do you go to the waterfall or continue further into the 🌳forest🌳?")
    await ctx.send("Which way do you go? (Type `!waterfall_again` or `!further_into_forest`)")

@bot.command()
async def waterfall_again(ctx):
    with open('waterfall.jpg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You have reached the waterfall again.")
        await ctx.send("Do you choose to go and explore the cave behind the waterfall or continue your journey into the 🌳forest🌳?")
        await ctx.send("(Type `!further_into_forest` or `!go_to_cave`)")

@bot.command()
async def further_into_forest(ctx):
    with open('forest.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You continue walking further into the 🌳forest🌳.You walk for many hours before you notice that you are walking in circles.")
        await ctx.send("You realise that you are lost. With no way to go anywhere, even back to Quazawaaka, you wander around the 🌳forest🌳 for days until you finally collapse and die :( . ")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def save_person(ctx):

    await ctx.send("You manage to save the person just in time. The person thanks you profusely. From the shadows nearby a slender, ethereal figure appears. A forest spirit🧝, you recognise. She thanks you for saving her friend and as a reward gives you a large coin🪙 with a map🗺️ engraved on it. 'This will take you to what you require in your journey', she says and disappears with her friend.")
    await ctx.send("You start following the map🗺️ on the coin🪙 until you reach a mysterious shop in the middle of nowhere. Do you enter the shop or continue following the map🗺️? ")
    await ctx.send("(Type `!enter_shop` or `!follow_map`)")

@bot.command()
async def follow_map(ctx):

    await ctx.send("You walk for a long time before you reach a field of huge tulip like flowers. In the middle of the field you can see a necklace📿 on a pedestal. A stone carving nearby proclaims that the necklace📿 heals its wearer of any life-threatening injuries.")
    await ctx.send("You remember what the forest spirit🧝 said and decide that the necklace📿 would be useful for the journey. Will you enter the field or go further into the 🌳forest🌳?")
    await ctx.send("(Type `!enter_field` or `!further_into_forest`)")

@bot.command()
async def enter_field(ctx):
    with open('field_of_flowers.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You enter the field just for the plants to start moving and strangle you. They choke you until you die. :( )")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def enter_shop(ctx):
    with open('magical_shop.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("The door creaks as you enter the shop. The place is dusty and quiet. On a window there is an old paper stuck which says that to take anything from the shop something has to be exchanged in return. You browse through the items till you notice that the sword🗡️ that had sunk into the river is present here.")
        await ctx.send("You realise that you can exchange the coin🪙 for the sword🗡️ or try to steal it as you are sure that you will require the sword🗡️ in your journey. What will you do?")
        await ctx.send("(Type `!exchange_coin` or `!steal_sword`)")

@bot.command()
async def steal_sword(ctx):

    await ctx.send("When you try to steal the sword🗡️, you start feeling very dizzy. You manage to take the sword🗡️ just to collapse right outside the door of the shop. The shop said something has to be exchanged. In your last moments you realise that by stealing you have essentially exchanged you soul, then you die. :( )")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def exchange_coin(ctx):

    await ctx.send("You quickly memorize the map🗺️ and exchange the coin🪙. You take the sword🗡️, exit the shop and follow the map🗺️ until you reach a field of huge tulip like flowers. In the middle of the field you can see a necklace📿 on a pedestal. A stone carving nearby proclaims that the necklace📿 heals its wearer of any life-threatening injuries.")
    await ctx.send("You remember what the forest spirit🧝 said and decide that the necklace📿 would be useful for the journey. Will you go into the field or go further into the 🌳forest🌳?")
    await ctx.send("(Type `!go_into_field` or `!further_into_forest`)")

@bot.command()
async def go_into_field(ctx):
    with open('field_of_flowers.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You enter the field just for the plants to start moving and strangle you. You cut down the plants with your sword🗡️ and manage to go and grab the neckalce. You wear the necklace📿 and it heals you. You continue walking in the 🌳forest🌳 until you hear the waterfall again.")
        await ctx.send("Will you go to the waterfall or go further into the forest?")
        await ctx.send("(Type `!go_to_waterfall_again` or `!further_into_forest`)")

@bot.command()
async def go_to_waterfall_again(ctx):
    with open('waterfall.jpg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You have reached the waterfall again.")
        await ctx.send("Do you choose to go and explore the cave behind the waterfall or go further into the 🌳forest🌳?")
        await ctx.send("(Type `!further_into_forest` or `!go_into_cave`)")

@bot.command()
async def go_into_cave(ctx):
    with open('field_of_flowers.jpeg', 'rb') as f:
    # Create a discord.File object with the image
        file = discord.File(f)
      
        # Send the image as a response to the message
        await ctx.send(file=file)
        if know==False:
            await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as a huge monster👺 appears. You then realise that this monster👺 is the reason that the villagers of Quazawaaka have disappeared.")
        else:
            await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as the monster👺 appears.")
        await ctx.send("Do you escape into the 🌳forest🌳 or fight the monster👺?")
        await ctx.send("(Type `!further_into_forest` or `!fight_the_monster`)")

@bot.command()
async def fight_the_monster(ctx):
    await ctx.send("To start the battle type `!fight start`. To attack the monster type `!fight sword` and to heal yourself type `!fight necklace`.")


# Global variables
user_hp = 2
monster_hp = 5

# Function to check if the game is over
def check_game_over():
    return user_hp <= 0 or monster_hp <= 0

# Function to reset the game
def reset_game():
    global user_hp, monster_hp
    user_hp = 2
    monster_hp = 5

# Command to handle the fight
@bot.command()
async def fight(ctx, action: str):
    global user_hp, monster_hp

    if action == 'start':
        reset_game()
        await ctx.send("Battle started! \nMonster HP: 5, Your HP: 2")

    elif action == 'sword':
        if check_game_over():
            await ctx.send("Game is already over. Please start a new game with !start")
            return

        monster_hp -= 2
        user_hp -= 1

        await ctx.send(f"You attacked! Monster HP: {monster_hp}, Your HP: {user_hp}")

        if check_game_over():
            if user_hp <= 0 and monster_hp<=0:
                await ctx.send("You have dealt the final blow. Both you and the monster die at the same time.")
                await ctx.send("The villagers were first worried about how you never returned but soon realised that no one went missing anymore. They realised that you gave your life to save theirs. The villagers of Quazawaaka live happily ever after. This day every year they gather around and mourn your death and thank you for your services.")
            elif user_hp<=0:
                await ctx.send("The monster👺 grabs you, breaks you in half and gobbles you up.You died :(.")
                await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")
            else:
                await ctx.send("You deliver the final blow. The monster died. Victory is yours")
                await ctx.send("You return to Quazawaaka and announce to the villagers that they are safe now. The villagers thank you and as a show of gratitude, give you enough money to celebrate for a week.")
                await ctx.send("The villagers of Quazawaaka live happily ever after. They gather around every year on this day to tell the tale of a valiant adventurer 🧙 who saved them from doom.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")
            reset_game()

    elif action == 'necklace':
        if check_game_over():
            await ctx.send("Game is already over. Please start a new game with !start")
            return

        if user_hp >= 2:
            await ctx.send("Your HP is already at maximum.")
            return

        user_hp += 1
        await ctx.send(f"You healed! User HP: {user_hp}")

    else:
        await ctx.send("Invalid action. You can only use `fight! sword`, fight! necklace`.")


@bot.command()
async def go_to_house(ctx):
    with open('abandoned_house.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
    await ctx.send("After entering the house you see a sphinx👹 standing there, watching you. It comes closer to you and declares that you have to answer its riddles🧩, otherwise it will kill you.")
    await ctx.send("You know that you cannot escape it so you have to answer its riddles🧩.")
    await ctx.send("`Each riddle🧩 will have a time limit of 10 seconds.`")
    await ctx.send("(Type `!riddle1` for the 1st riddle🧩.)")

@bot.command()
async def riddle1(ctx):

    await ctx.send("`I'm a guide without a voice, showing paths both near and far,\nI'm filled with lines and symbols, showing places high and low,\nYou'll need me on an adventure, whether by foot, plane, or car.\nWith me, you'll never lose your way, no matter where you go.\nAm I a compass, a map, a chart or a star?\n`")
    await ctx.send("(Type !compass or !map or !chart or !star)")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and isinstance(message.content, str)
    try:
        await bot.wait_for('message', timeout=15, check=check)

    except asyncio.TimeoutError:
        await ctx.send("You took too long to guess. The sphinx👹 gets impatient and gobbles you up. You died. :( .")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")


@bot.command()
async def compass(ctx):
    
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def chart(ctx):
    
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def star(ctx):
    
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")


@bot.command()
async def map(ctx):
    
    await ctx.send("'Hmm. The answer is correct.', says the the sphinx👹. 'Answer the second riddle🧩 and I'll let you go.' ")
    await ctx.send("It eyes you with a shrewd interest and starts with the second riddle🧩.")
    await ctx.send("(Type `!riddle2` for the 2nd riddle🧩.)")

@bot.command()
async def riddle2(ctx):
    #timer
    await ctx.send("`I'm often flipped but never tossed,\nIn pockets or jars, I'm often lost.\nI have two sides, heads and tails,\nYet I'm not part of any scales.\nWhat am I? A marble, dice, coin or button?\nAnswer fast before you become nothing but mutton.\n`")
    await ctx.send("(Type `!marble` or `!dice` or `!coin` or `!button`)")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and isinstance(message.content, str)
    try:
        await bot.wait_for('message', timeout=15, check=check)

    except asyncio.TimeoutError:
        await ctx.send("You took too long to guess. The sphinx👹 gets impatient and gobbles you up. You died. :( .")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")


@bot.command()
async def marble(ctx):
    
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def dice(ctx):
    
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def button(ctx):
    
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")

@bot.command()
async def coin(ctx):
    
    await ctx.send("The sphinx👹 looks surprised. 'For over a century no one has been able to answer both the riddles🧩 correctly. Since you have impresses me I will not only let you go but also tell you that the answer to these riddles🧩 will help you in your journey. Farewell adventurer 🧙'")
    await ctx.send("You leave from the house. As you walk in the 🌳forest🌳 you feel a prickling feeling on the back of your neck, like someone is watching you. You yell,'Who is there? Show yourself.' A slender, ethereal figure emerges from the shadow. A forest spirit🧝 you realise.")
    await ctx.send("Do you talk to the forest spirit🧝 or do you ignore her and walk away, further into the 🌳forest🌳 ?")
    await ctx.send("(Type `!talk_to_spirit` or `!further_into_forest`)")


@bot.command()
async def talk_to_spirit(ctx):
    with open('forest_spirit.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("You look at her a bit apprehensively and ask her,' Do you have any idea of an object that might help with my journey to save the villagers of Quazawaaka? Like maybe a coin🪙 or a map🗺️ or something?' She looks at you with an amused expression and says, 'Perhaps, perhaps not. Why should I help you? What will I gain from this?' You feel frustration building up in you.")
        await ctx.send("You wonder if she will accept any sort of deal.")
        await ctx.send("Do you make a deal or leave the forest spirit🧝 and walk away, further into the 🌳forest🌳 ?")
        await ctx.send("(Type `!make_deal` or `!further_into_forest`)")


@bot.command()
async def make_deal(ctx):
    
    await ctx.send("You say,'How about we make a deal?' The forest spirit🧝 laughs and says, 'Yes. I will give you this coin🪙 with a map🗺️ engraved on it. Follow the map🗺️ and get me a flower of the plants that bloom there.'")
    await ctx.send("You accept the deal and the coin🪙. As you follow the map🗺️, you encounter a person on your way. They happen to have a sword🗡️ which is designed to kill anything. You know that you will require it for your journey.")
    await ctx.send("When you ask for the sword🗡️ , they say,'No, I earned this sword🗡️. If you want it, you must earn it.'")
    await ctx.send("(Type `!fight_person` )")

@bot.command()
async def fight_person(ctx):
    await ctx.send("'Ok fine. How do I earn it?', you ask. The person says,'Both of us will guess a number from 1 to 5 (1 and 5 are included),whoever guesses the higher number will win.' 'Isn't that luck based?'you retort.")
    await ctx.send("  They ignore your comment and continue,'If you lose I will kill you, if you win you may take the sword🗡️.'you have no choice but to agree.")
    await ctx.send("(Type `!guess (the number you are guessing)`)")
@bot.command()
async def guess(ctx, user_guess: int):
    person_guess = random.randint(1, 5)
    
    if user_guess >= person_guess:
        await ctx.send("You guessed correctly and obtained the sword from the person")
        with open('field_of_flowers.jpeg', 'rb') as f:
        # Create a discord.File object with the image
            file = discord.File(f)
        
        # Send the image as a response to the message
            await ctx.send(file=file)
            await ctx.send("You continue following the map🗺️ and reach a field of tulip like flowers. As you go to cut the flower, in the middle of the field you can see a necklace📿 on a pedestal. A stone carving nearby proclaims that the necklace📿 heals its wearer of any life-threatening injuries. You start moving to the middle of the field just for the plants to start moving and strangle you. You cut down the plants with your sword🗡️ and manage to go and grab the neckalce.")
        await ctx.send("Type `!go_to_spirit` to return to the forest spirit🧝 again.")

    else:
        await ctx.send("Oh no! Your guess was incorrect. The person's guess was higher. They behead you. You die :( .)")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing `!start`.")
    

@bot.command()
async def go_to_spirit(ctx):
    with open('forest_spirit.jpeg', 'rb') as f:
        # Create a discord.File object with the image
        file = discord.File(f)
        
        # Send the image as a response to the message
        await ctx.send(file=file)
        await ctx.send("The forest spirit🧝 simply grins when she sees you come back, wearing the necklace📿. 'If you want to make another deal, you know who to look for.', she says as you hand over the flower and coin🪙. You simply walk away from there. As you continue your journey you hear the waterfall again")
        await ctx.send("Will you go to the waterfall or go further into the 🌳forest🌳?")
        await ctx.send("(Type `!go_to_waterfall_again` or `!further_into_forest`)")






bot.run(configure.DISCORD_TOKEN)