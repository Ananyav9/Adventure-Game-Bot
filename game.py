import discord
from discord.ext import commands
import configure
import random
import asyncio



intents=discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)
@bot.event#as soon as bot is online
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

know=False
number=0
nu=0
#Introduction
@bot.tree.command()
async def start_game(inter: discord.Interaction):
    await inter.channel.purge(limit=1)
    embed=discord.Embed(title="Welcome to this adventure game 🎮!",description="In this game 🎮 you are a famous adventurer 🧙 .You stumbled upon a village named 'Quazawaaka' near a 🌳forest🌳. The villagers tell you about how people keep disappearing in this 🌳forest🌳. The 🌳forest🌳 is vital for daily activties, and hence the people of Quazawaaka ask you for your help.\n`Remember you need to find 3 objects which will help you in your journey.`\n\n Type !start to start the adventure!!",colour=discord.Color.gold())

    await inter.response.defer(thinking=True)
    await inter.followup.send(embed=embed)
#to start game
@bot.command()
async def start(ctx):
    await ctx.channel.purge(limit=2)
    with open('forest.png', 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("You venture into the dark 🌳forest🌳 encounter a fork in the path. On one side you can see an abandoned house, on the other side you can hear roar of a waterfall.")
        await ctx.send("Which way do you go?")
        await ctx.send("(Type !go_to_house or !go_to_waterfall)")

@bot.command()
async def go_to_waterfall(ctx):
    await ctx.channel.purge(limit=5)
    with open('waterfall.jpg', 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("You have reached the waterfall. Behind the wall of flowing water, slightly obscured by mist is a cave.")
        await ctx.send("Do you choose to go and explore the cave or continue your journey into the 🌳forest🌳?")
        await ctx.send("(Type !continue_in_forest or !go_to_cave)")

@bot.command()
async def go_to_cave(ctx):
    await ctx.channel.purge(limit=5)
    with open('cave.png', 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as a huge monster👺 appears. You then realise that this monster👺 is the reason that the villagers of Quazawaaka have disappeared.")
        await ctx.send("Do you escape into the 🌳forest🌳 or fight the monster👺?")
        await ctx.send("(Type !escape_to_forest or !fight_monster)")

@bot.command()
async def fight_monster(ctx):
    await ctx.channel.purge(limit=5)
    
    await ctx.send("You run and attack the monster👺 just to realise that you don't have the right weapons to fight the monster👺.")
    await ctx.send("The monster👺 grabs you, breaks you in half and gobbles you up.You died :(.")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def escape_to_forest(ctx):
    await ctx.channel.purge(limit=5)
    know=True
    with open('forest.png', 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("As you continue your journey in the the 🌳forest🌳 you see a person drowning in a turbulent river. ")
        await ctx.send("Do you save the person or go further into the forest. What do you do?")
        await ctx.send("(Type !save_person or !further_into_forest)")
        number=4

@bot.command()
async def continue_in_forest(ctx):
    await ctx.channel.purge(limit=5)
    with open('river.png', 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("As you continue your journey in the the 🌳forest🌳 you see a person drowning in a turbulent river. ")
        await ctx.send("Do you save the person or go further into the forest. What do you do?")
        await ctx.send("(Type !save_person or !further_into_forest)")
        number=4

@bot.command()
async def further_into_forest(ctx):
    await ctx.channel.purge(limit=number+1)
    with open('forest.png', 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("You continue walking further into the 🌳forest🌳.You walk for many hours before you notice that you are walking in circles.")
        await ctx.send("You realise that you are lost. With no way to go anywhere, even back to Quazawaaka, you wander around the 🌳forest🌳 for days until you finally collapse and die :( . ")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def save_person(ctx):
    await ctx.channel.purge(limit=5)
    await ctx.send("You decide to swim and rescue the person who has by now gone underwater.")
    await ctx.send("(Type !rescue start to start saving the person.)")

RIVER_SIZE = 3


PERSON_POSITION = (0, 0)
DPERSON_POSITION = (random.randint(1, RIVER_SIZE-1), random.randint(1, RIVER_SIZE-1))


def generate_river(size, person_position, dperson_position):
    river = [["▓" for _ in range(size)] for _ in range(size)]
    river[person_position[0]][person_position[1]] = "🏊‍♂"
    river[dperson_position[0]][dperson_position[1]] = "▓"
    
    return river

def river_to_string(river):
    return "\n".join("".join(row) for row in river)

@bot.command()
async def rescue(ctx,action:str):
    global PERSON_POSITION
    if action=="start":
        await ctx.channel.purge(limit=3)
        river = generate_river(RIVER_SIZE, PERSON_POSITION, DPERSON_POSITION)
        await ctx.send("You (🏊‍♂) are trying to rescue a person (invisible) from drowning.")
        await ctx.send("Type !rescue up, !rescue down, !rescue left, !rescue right to navigate")
        
        await ctx.send(river_to_string(river))
    elif action=="up":
        await ctx.channel.purge(limit=2)
        if PERSON_POSITION[0] > 0:
            PERSON_POSITION = (PERSON_POSITION[0] - 1, PERSON_POSITION[1])
            river = generate_river(RIVER_SIZE, PERSON_POSITION, DPERSON_POSITION)
            
            await ctx.send(river_to_string(river))
        else:
            await ctx.send("You cannot move up!")
    elif action=="down":
        await ctx.channel.purge(limit=2)
        if PERSON_POSITION[0] < RIVER_SIZE - 1:
            PERSON_POSITION = (PERSON_POSITION[0] + 1, PERSON_POSITION[1])
            river = generate_river(RIVER_SIZE, PERSON_POSITION, DPERSON_POSITION)
            
            await ctx.send(river_to_string(river))
        else:
            await ctx.send("You cannot move down!")
    elif action=='left':
        await ctx.channel.purge(limit=2)
        if PERSON_POSITION[1] > 0:
            PERSON_POSITION = (PERSON_POSITION[0], PERSON_POSITION[1] - 1)
            river = generate_river(RIVER_SIZE, PERSON_POSITION, DPERSON_POSITION)
            
            await ctx.send(river_to_string(river))
        else:
            await ctx.send("You cannot move left!")
    elif action=='right':
        await ctx.channel.purge(limit=2)
        if PERSON_POSITION[1] < RIVER_SIZE - 1:
            PERSON_POSITION = (PERSON_POSITION[0], PERSON_POSITION[1] + 1)
            river = generate_river(RIVER_SIZE, PERSON_POSITION, DPERSON_POSITION)
            
            await ctx.send(river_to_string(river))
        else:
            await ctx.send("You cannot move right!")
    
    if PERSON_POSITION==DPERSON_POSITION:
        await ctx.channel.purge(limit=1)
        await ctx.send("You have successfully saved the person.As the person thanks you,a forest spirit appears at their side.She says'Thank you for rescuing my friend and in return I shall give you something that will help you in your journey.'\n She gives you a coin with a map engraved on it. ")
        await ctx.send("(Type !enter_shop' or `!follow_map)")

@bot.command()
async def follow_map(ctx):
    await ctx.channel.purge(limit=5)
    await ctx.send("You walk for a long time before you reach a field of huge tulip like flowers. In the middle of the field you can see a necklace📿 on a pedestal. A stone carving nearby proclaims that the necklace📿 heals its wearer of any life-threatening injuries.")
    await ctx.send("You remember what the forest spirit🧝 said and decide that the necklace📿 would be useful for the journey. Will you enter the field or go further into the 🌳forest🌳?")
    await ctx.send("(Type !enter_field or !further_into_forest)")
    number=3

@bot.command()
async def enter_field(ctx):
    await ctx.channel.purge(limit=4)
    with open('field_of_flowers.png', 'rb') as f:

        file = discord.File(f)

        await ctx.send(file=file)
        await ctx.send("You enter the field just for the plants to start moving and strangle you. They choke you until you die. :( )")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def enter_shop(ctx):
    await ctx.channel.purge(limit=5)
    with open('magical_shop.png', 'rb') as f:

        file = discord.File(f)

        await ctx.send(file=file)
        await ctx.send("The door creaks as you enter the shop. The place is dusty and quiet. On a window there is an old paper stuck which says that to take anything from the shop something has to be exchanged in return. You browse through the items till you notice that the scythe🗡 that had sunk into the river is present here.")
        await ctx.send("You realise that you can exchange the coin🪙 for the scythe🗡 or try to steal it as you are sure that you will require the scythe🗡 in your journey. What will you do?")
        await ctx.send("(Type !exchange_coin or !steal_scythe)")

@bot.command()
async def steal_scythe(ctx):
    await ctx.channel.purge(limit=5)

    await ctx.send("When you try to steal the scythe🗡, you start feeling very dizzy. You manage to take the scythe🗡 just to collapse right outside the door of the shop. The shop said something has to be exchanged. In your last moments you realise that by stealing you have essentially exchanged you soul, then you die. :( )")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def exchange_coin(ctx):
    await ctx.channel.purge(limit=5)

    await ctx.send("You quickly memorize the map🗺 and exchange the coin🪙. You take the scythe🗡, exit the shop and follow the map🗺 until you reach a field of huge tulip like flowers. In the middle of the field you can see a necklace📿 on a pedestal. A stone carving nearby proclaims that the necklace📿 heals its wearer of any life-threatening injuries.")
    await ctx.send("You remember what the forest spirit🧝 said and decide that the necklace📿 would be useful for the journey. Will you go into the field or go further into the 🌳forest🌳?")
    await ctx.send("(Type !go_into_field or !further_into_forest)")
    number=3

@bot.command()
async def go_into_field(ctx):
    await ctx.channel.purge(limit=4)
    with open('field_of_flowers.png', 'rb') as f:

        file = discord.File(f)

        await ctx.send(file=file)
        await ctx.send("You enter the field just for the plants to start moving and strangle you. You cut down the plants with your scythe🗡 and manage to go and grab the neckalce. You wear the necklace📿 and it heals you. You continue walking in the 🌳forest🌳 until you hear the waterfall again.")
        await ctx.send("Will you go to the waterfall or go further into the forest?")
        await ctx.send("(Type !go_to_waterfall_again or !further_into_forest)")
        number=4

@bot.command()
async def go_to_waterfall_again(ctx):
    await ctx.channel.purge(limit=5)
    with open('waterfall.jpg', 'rb') as f:

        file = discord.File(f)
        

        await ctx.send(file=file)
        await ctx.send("You have reached the waterfall again.")
        await ctx.send("Do you choose to go and explore the cave behind the waterfall or go further into the 🌳forest🌳?")
        await ctx.send("(Type !further_into_forest or !go_into_cave)")
        number=4

@bot.command()
async def go_into_cave(ctx):
    await ctx.channel.purge(limit=5)
    with open('cave.png', 'rb') as f:

        file = discord.File(f)
      

        await ctx.send(file=file)
        if know==False:
            await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as a huge monster👺 appears. You then realise that this monster👺 is the reason that the villagers of Quazawaaka have disappeared.")
        else:
            await ctx.send("As you enter the cave, you can see bones laying around and the smell of rot permeates the air. Suddenly you hear a groan.You hide behind a rock just as the monster👺 appears.")
        await ctx.send("Do you escape into the 🌳forest🌳 or fight the monster👺?")
        await ctx.send("(Type !further_into_forest or !fight_the_monster)")
        number=4

@bot.command()
async def fight_the_monster(ctx):
    await ctx.channel.purge(limit=5)
    await ctx.send("To start the battle type !fight start. To attack the monster type !fight scythe and to heal yourself type !fight necklace.")


user_hp = 2
monster_hp = 5


def check_game_over():
    return user_hp <= 0 or monster_hp <= 0


def reset_game():
    global user_hp, monster_hp
    user_hp = 2
    monster_hp = 5


@bot.command()
async def fight(ctx, action: str):
    global user_hp, monster_hp

    if action == 'start':
        reset_game()
        await ctx.send("Battle started! \nMonster HP: 5, Your HP: 2")

    elif action == 'scythe':
        await ctx.channel.purge(limit=2)
        if check_game_over():
            await ctx.send("Game is already over. Please start a new game with !start")
            return

        monster_hp -= 2
        user_hp -= 1

        await ctx.send(f"You attacked! Monster HP: {monster_hp}, Your HP: {user_hp}")

        if check_game_over():
            await ctx.channel.purge(limit=3)
            if user_hp <= 0 and monster_hp<=0:
                await ctx.send("You have dealt the final blow. Both you and the monster die at the same time.")
                await ctx.send("The villagers were first worried about how you never returned but soon realised that no one went missing anymore. They realised that you gave your life to save theirs. The villagers of Quazawaaka live happily ever after. This day every year they gather around and mourn your death and thank you for your services.\n \n The End.. \n \n You can play the game 🎮 again by typing !start")
            elif user_hp<=0:
                await ctx.send("The monster👺 grabs you, breaks you in half and gobbles you up.You died :(.")
                await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start")
            else:
                await ctx.send("You deliver the final blow. The monster died. Victory is yours")
                await ctx.send("You return to Quazawaaka and announce to the villagers that they are safe now. The villagers thank you and as a show of gratitude, give you enough money to celebrate for a week.")
                await ctx.send("The villagers of Quazawaaka live happily ever after. They gather around every year on this day to tell the tale of a valiant adventurer 🧙 who saved them from doom.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start")
            reset_game()

    elif action == 'necklace':
        await ctx.channel.purge(limit=2)
        if check_game_over():
            await ctx.send("Game is already over. Please start a new game with !start")
            return

        if user_hp >= 2:
            
            await ctx.send("Your HP is already at maximum.")
            return

        user_hp += 1
        
        await ctx.send(f"You healed! Your HP: {user_hp}")

    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("Invalid action. You can only use fight! scythe, fight! necklace`.")


@bot.command()
async def go_to_house(ctx):
    await ctx.channel.purge(limit=4)
    with open('abandoned_house.png', 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)
    await ctx.send("After entering the house you see a sphinx👹 standing there, watching you. It comes closer to you and declares that you have to answer its riddles🧩, otherwise it will kill you.")
    await ctx.send("You know that you cannot escape it so you have to answer its riddles🧩.")
    await ctx.send("Each riddle🧩 will have a time limit of 10 seconds and you can answer them only once.")
    await ctx.send("(Type !riddle1 for the 1st riddle🧩.)")

@bot.command()
async def riddle1(ctx):
    await ctx.channel.purge(limit=5)

    await ctx.send("I'm a guide without a voice, showing paths both near and far,places high and low,\nI'm filled with lines and symbols,\nYou'll need me on an adventure, whether by foot, plane, or car.\nWith me, you'll never lose your way, no matter where you go.\nAm I a compass, a map, a chart or a star?\n")
    await ctx.send("(Type !compass or !map or !chart or !star)")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and isinstance(message.content, str)
    try:
        await bot.wait_for('message', timeout=15, check=check)

    except asyncio.TimeoutError:
        await ctx.send("You took too long to guess. The sphinx👹 gets impatient and gobbles you up. You died. :( .")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")


@bot.command()
async def compass(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def chart(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def star(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")


@bot.command()
async def map(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("'Hmm. The answer is correct.', says the the sphinx👹. 'Answer the second riddle🧩 and I'll let you go.' ")
    await ctx.send("It eyes you with a shrewd interest and starts with the second riddle🧩.")
    await ctx.send("(Type !riddle2 for the 2nd riddle🧩.)")

@bot.command()
async def riddle2(ctx):
    await ctx.channel.purge(limit=4)

    await ctx.send("I'm often flipped but never tossed,\nIn pockets or jars, I'm often lost.\nI have two sides,you can also see me outside or inside the temples\nYet I'm not part of any scales.\nWhat am I? A marble, dice, coin or button?\nAnswer fast before you become nothing but mutton.\n")
    await ctx.send("(Type !marble or !dice or !coin or !button)")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and isinstance(message.content, str)
    try:
        await bot.wait_for('message', timeout=15, check=check)

    except asyncio.TimeoutError:
        await ctx.send("You took too long to guess. The sphinx👹 gets impatient and gobbles you up. You died. :( .")
        await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")


@bot.command()
async def marble(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def dice(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def button(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("'Ha! the answer is wrong.', the sphinx👹 proclaims and gobbles you up. You die :( .)")
    await ctx.send("The villagers of Quazawaaka continued to disappear until no remained. Later due to starvation even the monster👺 that kidnapped and ate the villagers in the 🌳forest🌳 died.  \n \n The End.. \n \n You can play the game 🎮 again by typing !start or quit the game by typing !close.")

@bot.command()
async def coin(ctx):
    await ctx.channel.purge(limit=3)
    await ctx.send("The sphinx👹 looks surprised. 'For over a century no one has been able to answer both the riddles🧩 correctly. Since you have impresses me I will not only let you go but also tell you that the answer to these riddles🧩 will help you in your journey. Farewell adventurer 🧙'")
    await ctx.send("You leave from the house. As you walk in the 🌳forest🌳 you feel a prickling feeling on the back of your neck, like someone is watching you. You yell,'Who is there? Show yourself.' A slender, ethereal figure emerges from the shadow. A forest spirit🧝 you realise.")
    await ctx.send("Do you talk to the forest spirit🧝 or do you ignore her and walk away, further into the 🌳forest🌳 ?")
    await ctx.send("(Type !talk_to_spirit or !further_into_forest)")
    number=4


@bot.command()
async def talk_to_spirit(ctx):
    await ctx.channel.purge(limit=5)
    with open('forest_spirit.png', 'rb') as f:

        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("You look at her a bit apprehensively and ask her,' Do you have any idea of an object that might help with my journey to save the villagers of Quazawaaka? Like maybe a coin🪙 or a map🗺 or something?' She looks at you with an amused expression and says, 'Perhaps, perhaps not. Why should I help you? What will I gain from this?' You feel frustration building up in you.")
        await ctx.send("You wonder if she will accept any sort of deal.")
        await ctx.send("Do you make a deal or leave the forest spirit🧝 and walk away, further into the 🌳forest🌳 ?")
        await ctx.send("(Type !make_deal or !further_into_forest)")
        number=5

@bot.command()
async def make_deal(ctx):
    await ctx.channel.purge(limit=6)
    
    await ctx.send("You say,'How about we make a deal?' The forest spirit🧝 laughs and says, 'Yes. I will give you this coin🪙 with a map🗺 engraved on it. Follow the map🗺 and get me a flower of the plants that bloom there.'")
    await ctx.send("You accept the deal and the coin🪙. As you follow the map🗺, you encounter a chamber.")
    await ctx.send("(Type !enter_chamber to enter the chamber. )")


SECRET_PATTERN = ['S', 'T', 'E','C', 'H', 'Y']
CORRECT_PATTERN = ['S','C','Y','T','H','E' ]


@bot.command()
async def enter_chamber(ctx):
    await ctx.channel.purge(limit=4)
    with open('chamber.jpeg', 'rb') as f:

        file = discord.File(f)
        await ctx.send(file=file)
        await ctx.send("You've entered a chamber adorned with ancient symbols.\nThese symbols seem to be arranged in a cryptic pattern. You have to rearrange the symbols to reveal the hidden word (and object)\n( Eg. if the letters given are P A P E L  then to enter the correct answer type !rearrange A P P L E)")


    await display_symbols(ctx, SECRET_PATTERN)


@bot.command()
async def rearrange(ctx, *symbols):
    nu+=1

    if list(symbols) == CORRECT_PATTERN :
        await ctx.send("You've successfully rearranged the symbols. You step back as the rocks collapse in front of you. When everything settles, the weapon, a scythe lies at your feet. You pick it up and go from here. You continue following the map🗺 and reach a field of tulip like flowers.")
        with open('field_of_flowers.png', 'rb') as f:
            file = discord.File(f)
            await ctx.send(file=file)
            await ctx.send("As you go to cut the flower, in the middle of the field you can see a necklace📿 on a pedestal. A stone carving nearby proclaims that the necklace📿 heals its wearer of any life-threatening injuries. You start moving to the middle of the field just for the plants to start moving and strangle you. You cut down the plants with your scythe🗡 and manage to go and grab the neckalce.")
        await ctx.send("Type !go_to_spirit to return to the forest spirit🧝 again.")
        nu=nu+7
    else:
        await ctx.send("Nothing happens. Looks like this isn't the correct pattern. To keep trying type !rearrange L E T T E R S I N T H E C O R R E C T O R D E R")


async def display_symbols(ctx, pattern):
    symbol_str = ' '.join((row) for row in pattern)

    await ctx.send(f"\n{symbol_str}\n")


@bot.command()
async def go_to_spirit(ctx):
    await ctx.channel.purge(limit=nu)
    with open('spirit_talking.png', 'rb') as f:
        file = discord.File(f)
        
        await ctx.send(file=file)
        await ctx.send("The forest spirit🧝 simply grins when she sees you come back, wearing the necklace📿. 'If you want to make another deal, you know who to look for.', she says as you hand over the flower and coin🪙. You simply walk away from there. As you continue your journey you hear the waterfall again")
        await ctx.send("Will you go to the waterfall or go further into the 🌳forest🌳?")
        await ctx.send("(Type !go_to_waterfall_again or !further_into_forest)")
        number=4


@bot.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def close(ctx):
    await bot.close()
    print("Bot Closed") 



bot.run(configure.DISCORD_TOKEN)