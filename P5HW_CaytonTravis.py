#Travis Cayton
#11/26/2024
#P5HW
#Using functions to create a game

import random


def display_inventory(inventory):
    """
    Counts and displays items in the inventory in the format 'Item xQuantity'.
    
    :param inventory: List of items in the inventory (e.g., ["Healing Potion", "Healing Potion", "Mana Potion"])
    """
    print("Inventory:")
    if not inventory:
        print("Your inventory is empty.")
        return

    # Count items and display them
    item_counts = {}
    for item in inventory:
        item_counts[item] = item_counts.get(item, 0) + 1
    
    for item, count in item_counts.items():
        print(f"{item} x{count}")

#This is a function to give the rooms a random name
def generate_room_name():
    """Generate a random name for the room."""
    room_names = [
        "Chamber of Shadows", "Hall of the Forgotten", "Crypt of Whispers",
        "Cavern of Doom", "Sanctum of the Brave", "Pit of Despair",
        "Vault of Secrets", "Arena of Chaos", "Den of Beasts",
        "Haven of Refuge", "Labyrinth of Trials", "Fortress of Fear",
        "Garden of Serenity", "Tomb of the Ancients", "Catacombs of Terror",
        "Spire of Eternity", "Altar of Blood", "Ruins of the Lost",
        "Temple of Silence", "Forest of Illusions", "Lake of Echoes",
        "Bridge of the Forgotten", "Canyon of Despair", "Mountain of Flame",
        "Valley of Shadows", "Desert of Time", "Sanctuary of Light",
        "Tower of Twilight", "Shrine of the Undying", "Library of Mysteries",
        "Dungeon of Trials", "Throne Room of the King", "Cave of Wonders",
        "Wasteland of Sorrows", "Crypt of the Undead", "Castle of Nightmares",
        "Arena of Valor", "Garden of Night", "Hall of Echoes",
        "River of Souls", "Plains of Fire", "Chamber of Secrets",
        "Room of the Forgotten Gods", "Corridor of Time", "Sanctuary of the Fallen",
        "Lair of the Dragon", "Grotto of Ice", "Chasm of Nightmares",
        "Furnace of Wrath", "Vault of Eternity", "Field of Ruin"
    ]
    return random.choice(room_names)


#This function is ran 1 to 3 times during generate_room():
def create_enemy():
    """Generate a random enemy with attributes and a unique name."""
    first_names = [
        # Non-fantasy names
        "Bob", "Tom", "Jerry", "Sue", "Jane", "Bill", "Jim", "Sam", "Pat", "Joe",
        "Nancy", "Ann", "Tim", "Rick", "Fred", "Lucy", "Maggie", "Frank", "Ted", "Kate",
        "Linda", "Betty", "Charlie", "Dave", "Eve", "Helen", "George", "Paul", "Chris", 
        "Mary", "John", "Carl", "Jack", "Diane", "Steve", "Martha", "Alan", "Ruth", 
        "Clara", "Bruce", "Ned", "Vince", "Laura", "Shirley", "Tommy", "Walt", "Ed", "Donna",
        
        # Fantasy-inspired names
        "Zug", "Lara", "Grak", "Morg", "Zena", "Thog", "Urza", "Drox", "Hilda", "Kron",
        "Vira", "Krag", "Mira", "Brun", "Skar", "Zal", "Droth", "Fen", "Lothar", "Gret",
        "Rok", "Yara", "Nok", "Xara", "Ulda", "Wren", "Tor", "Harn", "Vel", "Jor",
        "Fang", "Thorn", "Raz", "Luna", "Grim", "Zarn", "Kex", "Urog", "Bram", "Torg",
        "Brak", "Nina", "Ymir", "Vok", "Fira", "Zork", "Klint", "Brynn", "Zeth", "Lorn",
        "Zuna", "Harg", "Taz", "Orin", "Vex", "Zara", "Nora", "Drogar", "Mok", "Sigrid",

        # Everyday-modern names
        "Emma", "Liam", "Olivia", "Noah", "Sophia", "Mason", "Isabella", "Ethan", "Ava", 
        "Logan", "Mia", "Lucas", "Charlotte", "Elijah", "Amelia", "Benjamin", "Harper",
        "James", "Ella", "Henry", "Scarlett", "Alexander", "Lily", "Jackson", "Zoe", 
        "Owen", "Madison", "Ryan", "Chloe", "Luke", "Layla", "Aiden", "Ellie", "Wyatt",
        "Hannah", "Caleb", "Grace", "Connor", "Aubrey", "Nathan", "Aria", "Levi", "Sophie",
        "Jacob", "Natalie", "Hunter", "Stella", "David", "Lucy", "Evan", "Paisley", "Carter",

        # Mix-and-match names
        "Bjorn", "Ragnar", "Ingrid", "Freya", "Odin", "Skadi", "Fenrir", "Kara", "Volk",
        "Dagna", "Erik", "Sif", "Valka", "Hakon", "Sigurd", "Alva", "Elva", "Thor",
        "Astrid", "Magnus", "Leif", "Solveig", "Eivor", "Osk", "Vidar", "Ylva", "Gudrun",
        "Eirik", "Skoll", "Kael", "Lira", "Vryn", "Narek", "Jorvik", "Elgrim", "Cassie",
        "Shane", "Dan", "Milo", "Tess", "Jordan", "Brady", "Zoey", "Max", "Tina", "Dana",
        "Clyde", "Janet", "Vic", "Angie", "Pete", "Kyle", "Maddie", "Brody", "Elle", "Rob"
    ]

    enemy_types = [
        "Goblin", "Orc", "Skeleton", "Troll", "Bandit", "Necromancer", "Wraith", "Ghoul",
        "Warlock", "Dark Elf", "Spider", "Vampire", "Werewolf", "Zombie", "Shade", "Harpy",
        "Dragon", "Lich", "Giant", "Cyclops", "Basilisk", "Hydra", "Manticore", "Gorgon",
        "Imp", "Demon", "Succubus", "Banshee", "Kobold", "Slime", "Beastman", "Minotaur",
        "Wyvern", "Chimera", "Elemental", "Sorcerer", "Witch", "Hellhound", "Djinn",
        "Serpent", "Scorpion", "Worm", "Barbarian", "Pirate", "Assassin", "Thief", "Mummy",
        "Phantom", "Yeti", "Ice Wraith", "Sea Serpent", "Ooze", "Construct", "Golem",
        "Ettin", "Dryad", "Faerie", "Gremlin", "Siren", "Shadecaller", "Plague Rat",
        "Cursed Knight", "Bone Archer", "Shadow Stalker", "Death Hound", "Fire Drake",
        "Frost Giant", "Lava Spirit", "Forest Spirit", "Sky Serpent", "Nightmare"
    ]
    loot_table = ["healing potion", "magic scroll", "stat potion"]

    # Combine a random name with an enemy type
    enemy_name = f"{random.choice(first_names)} the {random.choice(enemy_types)}"
    health = random.randint(30, 100)
    strength = random.randint(1, 5)
    agility = random.randint(5, 8)
    intelligence = random.randint(1, 10)
    charisma = random.randint(1, 5)
    loot = random.sample(loot_table, k=random.randint(1, 3))  # Each enemy drops 1-3 items.
    
    enemy = {
        "Name": enemy_name,
        "Health": health,
        "Strength": strength,
        "Agility": agility,
        "Intelligence": intelligence,
        "Charisma": charisma,
        "Loot": loot
    }
    return enemy

#This function uses a for loop to draw the room based on a randomized size
def draw_room(room_grid,character, room):
    if character["Health"] > 0:
        """Draw the current state of the room."""
        print(room['Name'])
        for row in room_grid:
            print(" ".join(row))
        print()

#Here is where rooms are created and where size and number of enemies are defined
def generate_room():
    """Generate a room with a random number of enemies."""
    room_size = random.randint(5, 10)
    num_enemies = random.randint(1, 3)  # Random number of enemies (1-3)
    enemies = [create_enemy() for _ in range(num_enemies)]
    room_grid = [["." for _ in range(room_size)] for _ in range(room_size)]

    # Place the player at the starting position
    player_position = (0, 0)
    room_grid[player_position[1]][player_position[0]] = "🧍‍"

    # Place enemies randomly in the room
    enemy_positions = []
    for _ in range(num_enemies):
        while True:
            x, y = random.randint(0, room_size - 1), random.randint(0, room_size - 1)
            if (x, y) not in enemy_positions and (x, y) != player_position:  # Ensure no overlap
                enemy_positions.append((x, y))
                room_grid[y][x] = "💀"
                break

    room = {
        "Name": generate_room_name(),
        "Grid": room_grid,
        "Enemies": enemies,
        "Enemy Positions": enemy_positions,
        "Player Position": player_position
    }
    return room

#This function allows the player to move through the room grid with WASD and listens for when the player collides with an enemy
def move_player(room, direction, character):
    if character["Health"] > 0:
        """Move the player based on the WASD input."""
        x, y = room["Player Position"]
        room_size = len(room["Grid"])
        
        # Determine new position
        if direction == "W" and y > 0:  # Up
            y -= 1
        elif direction == "A" and x > 0:  # Left
            x -= 1
        elif direction == "S" and y < room_size - 1:  # Down
            y += 1
        elif direction == "D" and x < room_size - 1:  # Right
            x += 1
        else:
            print("Cannot move there")
            return room
            #generate_room()
        clean_screen()
        # Check for enemy interaction
        new_position = (x, y)
        if new_position in room["Enemy Positions"]:
            print("You've encountered an enemy!")
            enemy_index = room["Enemy Positions"].index(new_position)
            enemyInformation = fight_enemy_with_options(room["Player"], room["Enemies"][enemy_index])
            print()
            if character['Health'] > 0:
                print(f"You defeated {enemyInformation[0]}!")
                if "Nothing" in enemyInformation[1]:
                    print()
                else:
                    print(f"You looted: {', '.join(enemyInformation[1])}")
            print()
            room["Enemy Positions"].remove(new_position)  # Remove defeated enemy
            del room["Enemies"][enemy_index]  # Delete enemy from the list

        # Update room grid
        px, py = room["Player Position"]
        room["Grid"][py][px] = "."  # Clear old position
        room["Grid"][y][x] = "🧍‍"  # Mark new position
        room["Player Position"] = new_position
    return room

#This function handles all the action with the combat. Allows the player to FIGHT, ACT, or ITEM, and if the enemy is still alive, they will damage the player.
def fight_enemy_with_options(character, enemy):
    """Fight an enemy using the Act, Fight, or Item system with multiple random Act outcomes."""

    negative_act_outcomes = [
        "{character} attempted to seduce {enemy}, but was unsuccessful. How embarrassing!",
        "{character} tried to intimidate {enemy}, but {enemy} laughed in their face!",
        "{character} gave an impassioned speech to {enemy}, but it fell on deaf ears.",
        "{character} attempted to bribe {enemy} with a shiny rock. It didn't work.",
        "{character} started dancing to confuse {enemy}, but only confused themselves.",
        "{character} told a terrible joke to {enemy}, who seemed momentarily stunned.",
        "{character} offered a hug to {enemy}, but {enemy} attacked instead!",
        "{character} challenged {enemy} to a staring contest. It was awkward and ineffective.",
        "{character} claimed to be {enemy}'s long-lost sibling. {enemy} wasn't buying it.",
        "{character} loudly declared peace, but {enemy} charged at them anyway!"
    ]

    positive_act_outcomes = [
        "{character} attempted to seduce {enemy}, and {enemy} was smitten! They leave peacefully.",
        "{character} tried to intimidate {enemy}, and {enemy} fled in fear!",
        "{character} gave an inspiring speech to {enemy}, who decided to join your cause.",
        "{character} offered a shiny rock to {enemy}, and {enemy} accepted the bribe!",
        "{character} started dancing, and {enemy} joined in, forgetting about the fight.",
        "{character} told a joke so funny that {enemy} fell to the ground laughing and left.",
        "{character} offered a hug to {enemy}, and {enemy} surprisingly accepted before leaving.",
        "{character} challenged {enemy} to a staring contest and won, convincing them to surrender.",
        "{character} claimed to be {enemy}'s long-lost sibling, and {enemy} believed it!",
        "{character} declared peace, and {enemy} agreed to leave without a fight."
    ]
    
    print()
    print(f"\n{character['Name']} has encountered {enemy['Name']}!")
    enemy["Health"] = random.randint(30, 100)
    while character["Health"] > 0 and enemy["Health"] > 0:
        print()
        print(f"{enemy['Name']} (Health: {enemy['Health']})")
        print()
        print(f"{character['Name']} (Health: {character['Health']})")
        print()
        print()
        print("Actions:")
        print()
        print("1 = Fight")
        print("2 = Act")
        print("3 = Item")
        print()
        action = input("Choose an action (1/2/3): ")
        print()
        clean_screen()
        if action == "2":  # Act
            if character["Charisma"] > random.randint(0, 30):  # Player's Charisma in 30 chance of success
                act_outcome = random.choice(positive_act_outcomes).format(
                    character=character["Name"], enemy=enemy["Name"]
                )
                print(act_outcome)
                print()

                if "join your cause" in act_outcome:  # Example effect: adding enemy loot
                    print(f"{enemy['Name']} left behind their loot: {', '.join(enemy['Loot'])}.")
                    character["Items"].extend(enemy["Loot"])

                return [enemy['Name'], 'Nothing']
            else:
                act_outcome = random.choice(negative_act_outcomes).format(
                    character=character["Name"], enemy=enemy["Name"]
                )
                print(act_outcome)
                print()
                print(f"{enemy['Name']} isn't affected and attacks!")
                print()
        elif action == "1":  # Fight
            damage = character["Strength"] + random.randint(0, 5) # 0 to 5 + Player's Strength damage
            enemy["Health"] -= damage
            print(f"You dealt {damage} damage to the {enemy['Name']}.")

            
        elif action == "3":  # Item
            if character["Items"]:
                #print("Your items: " + ", ".join(character["Items"]))
                display_inventory(character["Items"])
                print()
                print()
                item = input("Choose an item to use: ").lower()
                if "healing potion" in item:
                    item = "healing potion"
                    if item in character["Items"]:
                        character["Health"] += 20
                        character["Health"] = min(character["Health"], 100)  # Cap health
                        print("You used a healing potion and restored 20 health!")
                        character["Items"].remove(item)
                    else:
                        print("You don't have that item or can't use it now.")
                if "magic scroll" in item:
                    item = "magic scroll"
                    if item in character["Items"]:
                        if character["Intelligence"] > 0:
                            damage = random.randint(5, 10) * character["Intelligence"]
                        else:
                            damage = random.randint(5, 10)
                        enemy["Health"] -= damage
                        print(f"Your magic scroll's spell dealt {damage} damage to {enemy['Name']}")
                        character["Items"].remove(item)
                    else:
                        print("You don't have that item or can't use it now.")
                if "stat potion" in item:
                    item = "stat potion"
                    if item in character["Items"]:
                        unspentStatPoints = 2
                        while unspentStatPoints > 0:
                            clean_screen()
                            print(f"Consuming the stat potion granted you 2 stat points!")
                            print(f"You have {unspentStatPoints} unspent stat points.")
                            print()
                            print(f"1 = Strength({character['Strength']})")
                            print()
                            print(f"2 = Agility({character['Agility']})")
                            print()
                            print(f"3 = Intelligence({character['Intelligence']})")
                            print()
                            print(f"4 = Charisma({character['Charisma']})")
                            print()
                            print()
                            statChoice = input("Choose a stat: ")

                            if statChoice == "1":
                                character['Strength'] = character['Strength'] + 1
                                
                            elif statChoice == "2":
                                character['Agility'] = character['Agility'] + 1

                            elif statChoice == "3":
                                character['Intelligence'] = character['Intelligence'] + 1

                            elif statChoice == "4":
                                character['Charisma'] = character['Charisma'] + 1

                            else:
                                invalidAnswer = True
                                while invalidAnswer == True:
                                    statChoice = input("ERROR, Choose another stat: ")
                                    if statChoice == "1":
                                        character['Strength'] = character['Strength'] + 1
                                        invalidAnswer = False
                                    elif statChoice == "2":
                                        character['Agility'] = character['Agility'] + 1
                                        invalidAnswer = False
                                    elif statChoice == "3":
                                        character['Intelligence'] = character['Intelligence'] + 1
                                        invalidAnswer = False
                                    elif statChoice == "4":
                                        character['Charisma'] = character['Charisma'] + 1
                                        invalidAnswer = False
                            unspentStatPoints = unspentStatPoints - 1
                        character["Items"].remove(item)
                    else:
                        print("You don't have that item or can't use it now.")
            else:
                print("You have no items to use.")
        else:
            print("Invalid action.")
        
        # Enemy attacks back
        if character["Agility"] > random.randint(0, 70): #Player's Agility in 70 chance of dodging an attack
            print(f"You dodged {enemy['Name']}'s attack!")
        else:
            if enemy["Health"] > 0:
                enemy_damage = enemy["Strength"] + random.randint(0, 5)
                character["Health"] -= enemy_damage
                print(f"The {enemy['Name']} attacked you for {enemy_damage} damage.")
        if character["Health"] <= 0:
            print("You were defeated!")
        if enemy["Health"] <= 0:

            character["Items"].extend(enemy["Loot"])

            return [enemy['Name'], enemy['Loot']]
            
#This function is because I got tired of seeing the previous text and it makes it feel more like a game this way
def clean_screen():
    print("\n" * 49)
    print("\n" * 49)


#Here is the create character function where the name and stats are chosen.
def create_character():

    name = input("Enter character's name: ")

    max_health = 100

    health = max_health

    inventory = ["magic scroll","healing potion"]

    unspentStatPoints = 10

    agility = 0

    strength = 0

    intelligence = 0

    charisma = 0

    

    while unspentStatPoints > 0:
        clean_screen()
        print()
        print(f"You have {unspentStatPoints} unspent stat points.")
        print()
        print(f"1 = Strength({strength})")
        print()
        print(f"2 = Agility({agility})")
        print()
        print(f"3 = Intelligence({intelligence})")
        print()
        print(f"4 = Charisma({charisma})")
        print()
        print()
        statChoice = input("Choose a stat: ")

        if statChoice == "1":
            strength = strength + 1
            
        elif statChoice == "2":
            agility = agility + 1

        elif statChoice == "3":
            intelligence = intelligence + 1

        elif statChoice == "4":
            charisma = charisma + 1

        else:
            invalidAnswer = True
            while invalidAnswer == True:
                statChoice = input("ERROR, Choose another stat: ")
                if statChoice == "1":
                    strength = strength + 1
                    invalidAnswer = False
                elif statChoice == "2":
                    agility = agility + 1
                    invalidAnswer = False
                elif statChoice == "3":
                    intelligence = intelligence + 1
                    invalidAnswer = False
                elif statChoice == "4":
                    charisma = charisma + 1
                    invalidAnswer = False
        unspentStatPoints = unspentStatPoints - 1
                

    
    character = {
        "Name" : name,
        "Health" : health,
        "Items" : inventory,
        "Strength" : strength,
        "Agility" : agility,
        "Intelligence" : intelligence,
        "Charisma" : charisma
        }

    
    return character

#This is the function that handles most of the room's gameplay outside of combat
def explore_room(character,room):
    """Explore the room with movement and interactions."""
    if character['Health'] > 0:
        #room = generate_room()
        room["Player"] = character  # Add the player to the room context

        print(f"\nYou have discovered the {room['Name']}!")
        print("\nUse WASD to move, and try to interact with enemies.")
        draw_room(room["Grid"],character, room)
        
        while character['Health'] > 0:
            action = input("Enter your move (W/A/S/D or E to enter a new room): ").upper()
            if action == "E":
                clean_screen()
                print("You teleport into a new room...")
                print()
                room = generate_room()
                room["Player"] = character  # Add the player to the room context
                draw_room(room["Grid"],character, room)
            elif action in ["W", "A", "S", "D"]:
                room = move_player(room, action, character)
                draw_room(room["Grid"],character, room)

                # Check if there are any enemies left
                if not room["Enemies"] and character['Health'] > 0:
                    print("The room is clear! You defeated all the enemies.")
                    print()          
            else:
                print("Invalid input. Please use W, A, S, D, or E.")

def displayCharacterStats(character):
    clean_screen()
    print("-------------------------------------")
    print(f"Name: {character['Name']}")
    print()
    print(f"Health: {character['Health']}")
    print()
    display_inventory(character['Items'])
    print()
    print(f"Strength: {character['Strength']}")
    print()    
    print(f"Agility: {character['Agility']}")
    print()
    print(f"Intelligence: {character['Intelligence']}")
    print()
    print(f"Charisma: {character['Charisma']}")
    print("-------------------------------------")
    print()
    print("Press Enter to Start!")
    
#Start the game and begin character creator
def main():
    clean_screen()
    print("Dungeon Decide")
    char1 = create_character()
    displayCharacterStats(char1)
    input()
    clean_screen()
    room = generate_room()
    explore_room(char1,room)
    if char1['Health'] <= 0:
        print(f"{char1['Name']} has died. GAME OVER")

#Call the main
if __name__ == "__main__":
    main()
