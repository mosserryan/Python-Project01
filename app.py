player = {
    "strength": 0,
    "intelligence": 0,
    "stamina": 0,
    "name": None,
    "race": None,
    "class": None
}

def chooseName():
    while player["name"] == None:
        userInput = input("\nChoose player's name: ")
        if len(userInput) < 12:
            break
        else:
            print("Player name must not exceed 12 characters.")
    player["name"] = userInput.capitalize()

def chooseRace():
    while player["race"] == None:
        userInput = input("\nChoose one of the following races, [Human, Elf, Orc]: ")
        if userInput.lower() == "human":
            player["strength"] += 10
            player["intelligence"] += 10
            player["stamina"] += 10
            break
        elif userInput.lower() == "elf":
            player["strength"] += 5
            player["intelligence"] += 10
            player["stamina"] += 15
            break
        elif userInput.lower() == "orc":
            player["strength"] += 20
            player["intelligence"] += 0
            player["stamina"] += 10
            break
        else:
            print(f'You typed "{userInput}", that is not a valid input, please choose a valid input.')
    player["race"] = userInput.capitalize()
    print(f"\n({player['race']}) {player['name']}'s current stats: \nStrength: {player['strength']} \nIntelligence: {player['intelligence']} \nStamina: {player['stamina']}")

def chooseClass():
    while player["class"] == None:
        userInput = input("\nChoose one of the following classes, [Warrior, Wizard, Ranger]: ")
        if userInput.lower() == "warrior":
            player["strength"] += 20
            player["intelligence"] += 5
            player["stamina"] += 10
            break
        elif userInput.lower() == "wizard":
            player["strength"] += 5
            player["intelligence"] += 20
            player["stamina"] += 10
            break
        elif userInput.lower() == "ranger":
            player["strength"] += 10
            player["intelligence"] += 10
            player["stamina"] += 15 
            break
        else:
            print(f'You typed "{userInput}", that is not a valid input, please choose a valid input.')
    player["class"] = userInput.capitalize()
    print(f"\n({player['race']}/{player['class']}) {player['name']}'s current stats: \nStrength: {player['strength']} \nIntelligence: {player['intelligence']} \nStamina: {player['stamina']}")

def confirm():
    while True:
        userInput = input("Finish creating new player? Type [Y/N]: ")
        if userInput.lower() == "y":
            print(f"\nNew player created! {player['name']} the {player['race']} {player['class']} \nStarting stats: \nStrength: {player['strength']} \nIntelligence: {player['intelligence']} \nStamina: {player['stamina']}.")
            break
        elif userInput.lower() == "n":
            player["name"] = None
            player["race"] = None
            player["class"] = None
            player["strength"] = 0
            player["intelligence"] = 0
            player["stamina"] = 0
            main()
            break
        else:
            print(f'You typed "{userInput}", that is not a valid input, please choose a valid input.')
            
    

def main():
    chooseName()
    chooseRace()
    chooseClass()
    confirm()

main()

# print("\nExiting program now.\n")
# print(f'\n You wrote "{userInput}", that is not a valid input.\n')

#Give user ability to go back to a chosen Name, Race, or Class at the end instead of repeating whole process.
#Give user ability to go back in general (before reaching confirmation stage).