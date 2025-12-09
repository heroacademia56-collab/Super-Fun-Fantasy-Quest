import pygame
import sys
import random

# ---------------- Sunset Splash ----------------
def draw_sunset_gradient(screen, resolution):
    width, height = resolution
    colors = ["#FF4500", "#FF6347", "#FFD700", "#FFA500", "#FF8C00", "#8B0000"]
    rgb_colors = [pygame.Color(c) for c in colors]
    step_height = height // len(rgb_colors)

    for i, color in enumerate(rgb_colors):
        rect = pygame.Rect(0, i * step_height, width, step_height)
        pygame.draw.rect(screen, color, rect)

def splash_screen():
    pygame.init()
    pygame.display.set_caption("Quest for the Sword of Power — Sunset Splash")
    clock = pygame.time.Clock()

    info = pygame.display.Info()
    resolution = (info.current_w, info.current_h)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

        draw_sunset_gradient(screen, resolution)

        # Title
        title_font = pygame.font.SysFont("Helvetica", 60, bold=True)
        title_surface = title_font.render("Quest for the Sword of Power", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(resolution[0] // 2, resolution[1] // 2 - 60))
        screen.blit(title_surface, title_rect)

        # Subtitle
        sub_font = pygame.font.SysFont("Helvetica", 28)
        sub_surface = sub_font.render("Press ENTER to begin your journey", True, (255, 255, 255))
        sub_rect = sub_surface.get_rect(center=(resolution[0] // 2, resolution[1] // 2 + 10))
        screen.blit(sub_surface, sub_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# ---------------- Text Adventure ----------------
inventory = []
stats = {"health": 20, "attack": 3, "cursed": False}

def adventure():
    print("\n=== Quest for the Sword of Power ===")
    name = input("What is your hero's name? ").strip() or "Nameless Hero"

    chapter_intro(name)
    chapter_allies_and_items(name)

    while True:
        path_choice = choose_path()
        result = resolve_path(path_choice, name)
        chapter_final_battle(result, name)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("\nThanks for playing! Goodbye.")
            break
        # Reset for replay
        inventory.clear()
        stats.update({"health": 20, "attack": 3, "cursed": False})

# ---- Chapters ----
def chapter_intro(name):
    print(f"\nWelcome, {name}. An evil monster threatens the kingdom.")
    print("Only the Sword of Power can save the realm!")
    print("You begin your journey at dusk as the last light fades.")

def chapter_allies_and_items(name):
    meet_companion(name)
    find_herbs()
    find_charm()

def chapter_final_battle(path_result, name):
    print("\n— Chapter IV: The Final Battle —")
    print("The monster attacks the capital. Bells toll, citizens flee...")
    ending(path_result, name)

# ---- Allies & Items ----
def meet_companion(name):
    print("\n— Chapter II: A Stranger on the Road —")
    print("You meet a wandering bard with a silver lute.")
    choice = input("Invite them to join you? (y/n): ").strip().lower()
    if choice in {"y", "yes"}:
        print("The bard joins you, boosting morale. You gain +1 attack.")
        inventory.append("Companion")
        stats["attack"] += 1
    else:
        print("You travel alone, the road feels heavier.")

def find_herbs():
    print("\nYou discover a patch of glowing moon-herbs by a brook.")
    choice = input("Gather the herbs? (y/n): ").strip().lower()
    if choice in {"y", "yes"}:
        print("The herbs restore your strength. You gain +5 health.")
        inventory.append("Healing Herbs")
        stats["health"] += 5
    else:
        print("You leave them untouched.")

def find_charm():
    print("\nAn old tinkerer offers a protective charm—for a price.")
    choice = input("Trade a favor for the charm? (y/n): ").strip().lower()
    if choice in {"y", "yes"}:
        print("You accept. The charm wards off minor curses.")
        inventory.append("Protective Charm")
    else:
        print("You decline. The path remains uncertain.")

# ---- Paths ----
def choose_path():
    print("\n— Chapter III: Trials of the Realm —")
    print("Choose your path:")
    print("1) Enter the Dark Forest (riddle)")
    print("2) Climb the Mountain of Trials (endurance roll)")
    print("3) Explore the Forgotten Cave (logic puzzle)")
    print("4) Investigate the Haunted Ruins (curse risk)")
    print("5) Cross the Mystic River (chance)")
    print("6) Visit the Marketplace (trade, upgrade)")
    choice = input("Enter 1, 2, 3, 4, 5, or 6: ").strip()
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
    elif choice == "6":
        return market_path(name)
    else:
        print("\nIndecision costs precious time. The monster grows stronger...")
        stats["health"] -= 2
        return "failure"

# (Forest, Mountain, Cave, Ruins, River, Market functions same as before...)

def forest_path(name):
    print("\nYou enter the Dark Forest. A spirit whispers a riddle:")
    print("'I speak without a mouth and hear without ears. What am I?'")
    answer = input("Your answer: ").strip().lower()
    if answer == "echo":
        print("The spirit rewards you with the Sword of Power!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The spirit vanishes. You wander lost.")
        stats["health"] -= 2
        return "failure"

def mountain_path(name):
    print("\nYou climb the Mountain of Trials. A blizzard strikes!")
    roll = random.randint(1, 6)
    print(f"You roll a fate die... {roll} (need 4+)")
    if roll >= 4:
        print("You endure the storm and find the Sword!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The storm forces you back down.")
        stats["health"] -= 3
        return "failure"

def cave_path(name):
    print("\nYou explore the Forgotten Cave. A chest awaits.")
    print("Puzzle lock: 2 + 2 * 2 = ?")
    answer = input("Your answer: ").strip()
    if answer == "6":
        print("The chest opens, revealing the Sword!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The chest remains sealed.")
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
        stats["cursed"] = True
        if "Protective Charm" in inventory:
            print("Your charm glows and absorbs the worst of the curse.")
            stats["cursed"] = False
        return "cursed" if stats["cursed"] else "failure"

def river_path(name):
    print("\nYou reach the Mystic River. Do you try to cross? (y/n)")
    choice = input("> ").strip().lower()
    if choice in {"y", "yes"}:
        roll = random.randint(1, 10)
        print(f"You roll a fate die... {roll} (need 6+)")
        if roll >= 6:
            print("You cross safely and find the Sword!")
            inventory.append("Sword of Power")
            return "sword"
        else:
            print("The river sweeps you away. You lose time and strength.")
            stats["health"] -= 4
            return "failure"
    else:
        print("You avoid the river, but miss the sword.")
        return "failure"
    
def market_path(name):
    print("\nYou visit the bustling marketplace.")
    print("A blacksmith offers to hone your blade. A healer offers a tonic.")
    print("1) Hone attack (+1 attack)")
    print("2) Drink tonic (+3 health)")
    print("3) Trade for lucky coin (reroll once on a failed check)")
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        stats["attack"] += 1
        print("Your strike grows truer. Attack +1.")
    elif choice == "2":
        stats["health"] += 3
        print("Warmth spreads through you. Health +3.")
    elif choice == "3":
        inventory.append("Lucky Coin")
        print("A coin that sometimes turns fate.")
    else:
        print("You browse but buy nothing.")
    return "market"

# ---- Endings ----
def ending(result, name):
    # Lucky Coin reroll mechanic
    if result == "failure" and "Lucky Coin" in inventory:
        print("\nYour Lucky Coin gleams... fate offers a second chance.")
        reroll = random.randint(1, 2)  # 50/50 save
        if reroll == 2:
            print("Fortune smiles! You stumble upon the Sword after all.")
            result = "sword"
        else:
            print("The coin grows cold. Fate remains unchanged.")

    print(f"\n{name} — Health: {stats['health']} | Attack: {stats['attack']} | Items: {', '.join(inventory) if inventory else 'None'}")

    print("\nThe monster looms over the capital, shadows coiling like smoke.")
    if result == "sword":
        narrative_victory(name)
    elif result == "cursed":
        narrative_cursed_victory(name)
    else:
        narrative_defeat(name)

def narrative_victory(name):
    bonus = stats["attack"]
    if "Companion" in inventory:
        print(f"\nThe bard’s song steadies {name}'s heart. Together you charge.")
        bonus += 1
    if "Healing Herbs" in inventory:
        print(f"{name} uses moon-herbs, pushing through pain.")
        stats["health"] += 2
    print(f"{name} raises the Sword of Power. Light cascades across the battlefield.")
    print(f"With attack {bonus}, the monster falters, shrieks, and collapses.")
    print("Victory! The kingdom is saved. Bards will sing this night for ages.")

def narrative_cursed_victory(name):
    print(f"\nThe curse threads through {name}'s veins—power and price intertwined.")
    print("The monster is slain, but the hero fades into mist, a bittersweet legend.")
    print("Some say the curse guards the realm still, unseen and eternal.")

def narrative_defeat(name):
    if stats["health"] <= 0:
        print(f"\nExhausted, {name} collapses as the city walls crumble.")
    else:
        print(f"\n{name} fights bravely, but without the sword, the monster prevails.")
    print("Defeat. Survivors whisper of a hero who nearly turned the tide.")

# ---------------- Run ----------------
if __name__ == "__main__":
    splash_screen()   # Wait for ENTER on the sunset splash
    adventure()       # Start the extended interactive story
