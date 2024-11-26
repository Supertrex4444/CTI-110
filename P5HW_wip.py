#Travis Cayton
#11/26/2024
#P5HW
#Using functions to create a game

def create_character():

    name = input("Enter character's name: ")

    health = input(f"Enter {name}'s health: ")

    inventory = []

    level = 1

    weapons = ["dagger"]

    strength = input(f"Enter {name}'s strength: ")

    
    character = {
        "Name" : name,
        "Health" : health,
        "Weapons" : weapons,
        "Items" : inventory,
        "Level" : level,
        "Strength" : strength
        }
    return character

def main():
    print("Game is starting...")

    char1 = create_character()

    print(char1)
    



if __name__ == "__main__":
    main()
