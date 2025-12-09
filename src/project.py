import random

inventory = []

def main():
    print("\n=== Quest for the Sword of Power ===")
    name = input("What is your hero's name? ").strip() or "Nameless Hero"
    intro(name)
    path = choose_path()
    result = resolve_path(path, name)
    ending(result, name)

def intro(name):
    print(f"\nWelcome, {name}. An evil monster threatens the kingdom.")
    print("Only the Sword of Power can save the realm!")

def choose_path():
    print("\nChoose your path:")
    print("1) Enter the Dark Forest")
    print("2) Climb the Mountain of Trials")
    print("3) Explore the Forgotten Cave")
    print("4) Investigate the Haunted Ruins")
    print("5) Cross the Mystic River")
    choice = input("Enter 1, 2, 3, 4, or 5: ").strip()
    return choice

def resolve_path(choice, name):
    if choice == "1":
        return forest_path(name)
    elif choice == "2":
        return mountain_path(name)
    elif choice == "3":
        return cave_path(name)
    elif choice == "4":
        return ruins_path(name)
    elif choice == "5":
        return river_path(name)
    else:
        print("\nIndecision costs precious time. The monster grows stronger...")
        return "failure"

def forest_path(name):
    print("\nYou enter the Dark Forest. A spirit whispers a riddle:")
    print("'I speak without a mouth and hear without ears. What am I?'")
    answer = input("Your answer: ").strip().lower()
    if answer == "echo":
        print("The spirit rewards you with the Sword of Power!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The spirit vanishes. You wander lost and empty-handed.")
        return "failure"

def mountain_path(name):
    print("\nYou climb the Mountain of Trials. A blizzard strikes!")
    roll = random.randint(1, 6)
    print(f"You roll a fate die... {roll}")
    if roll >= 4:
        print("You endure the storm and find the Sword at the summit!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The storm forces you back down the mountain.")
        return "failure"

def cave_path(name):
    print("\nYou explore the Forgotten Cave. Shadows dance on the walls.")
    print("You find a chest with a puzzle lock: 2 + 2 * 2 = ?")
    answer = input("Your answer: ").strip()
    if answer == "6":
        print("The chest opens, revealing the Sword of Power!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The chest remains sealed. You leave empty-handed.")
        return "failure"

def ruins_path(name):
    print("\nYou enter the Haunted Ruins. A ghost asks:")
    print("'What walks on four legs in the morning, two at noon, and three at night?'")
    answer = input("Your answer: ").strip().lower()
    if "man" in answer or "human" in answer:
        print("The ghost smiles and grants you the Sword of Power!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The ghost wails and curses your journey.")
        return "cursed"

def river_path(name):
    print("\nYou reach the Mystic River. Do you try to cross? (y/n)")
    choice = input("> ").strip().lower()
    if choice in {"y", "yes"}:
        roll = random.randint(1, 10)
        print(f"You roll a fate die... {roll}")
        if roll > 5:
            print("You cross safely and find the Sword!")
            inventory.append("Sword of Power")
            return "sword"
        else:
            print("The river sweeps you away. You lose your chance.")
            return "failure"
    else:
        print("You avoid the river, but miss the sword.")
        return "failure"

def ending(result, name):
    print("\nThe monster attacks the capital!")
    if result == "sword":
        print(f"{name} wields the Sword of Power. Light banishes the darkness!")
        print("Victory! The kingdom is saved!")
    elif result == "cursed":
        print(f"{name} fights with cursed strength. The monster is defeated, but the hero vanishes into legend...")
    else:
        print(f"{name} fights bravely, but without the sword, the monster prevails...")
        print("Defeat. The kingdom falls.")

def play_again():
    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    return choice in {"y", "yes"}

if __name__ == "__main__":
    while True:
        inventory.clear()
        main()
        if not play_again():
            print("\nThanks for playing! Goodbye.")
            break
