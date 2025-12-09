import pygame
import sys
import random

# ---------------- Sunset Splash ----------------
def draw_sunset_gradient(screen, resolution):
    """Draw a vertical sunset gradient background."""
    width, height = resolution
    colors = ["#FF4500", "#FF6347", "#FFD700", "#FFA500", "#FF8C00", "#8B0000"]
    rgb_colors = [pygame.Color(c) for c in colors]
    step_height = height // len(rgb_colors)

    for i, color in enumerate(rgb_colors):
        rect = pygame.Rect(0, i * step_height, width, step_height)
        pygame.draw.rect(screen, color, rect)

def splash_screen():
    pygame.init()
    pygame.display.set_caption("Sunset Splash")
    clock = pygame.time.Clock()

    info = pygame.display.Info()
    resolution = (info.current_w, info.current_h)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)

    running = True
    timer = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        draw_sunset_gradient(screen, resolution)

        font = pygame.font.SysFont("Helvetica", 48, bold=True)
        text_surface = font.render("Quest for the Sword of Power", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(resolution[0] // 2, resolution[1] // 2))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        dt = clock.tick(30)
        timer += dt
        if timer > 3000:  # auto-close after 3 seconds
            running = False

    pygame.quit()

# ---------------- Text Adventure ----------------
inventory = []

def adventure():
    print("\n=== Quest for the Sword of Power ===")
    name = input("What is your hero's name? ").strip() or "Nameless Hero"
    print(f"\nWelcome, {name}. An evil monster threatens the kingdom.")
    print("Only the Sword of Power can save the realm!")

    while True:
        print("\nChoose your path:")
        print("1) Enter the Dark Forest")
        print("2) Climb the Mountain of Trials")
        print("3) Explore the Forgotten Cave")
        print("4) Investigate the Haunted Ruins")
        print("5) Cross the Mystic River")
        choice = input("Enter 1, 2, 3, 4, or 5: ").strip()

        if choice == "1":
            result = forest_path(name)
        elif choice == "2":
            result = mountain_path(name)
        elif choice == "3":
            result = cave_path(name)
        elif choice == "4":
            result = ruins_path(name)
        elif choice == "5":
            result = river_path(name)
        else:
            print("Indecision costs precious time...")
            result = "failure"

        ending(result, name)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("\nThanks for playing! Goodbye.")
            break
        inventory.clear()

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
        return "failure"

def mountain_path(name):
    print("\nYou climb the Mountain of Trials. A blizzard strikes!")
    roll = random.randint(1, 6)
    print(f"You roll a fate die... {roll}")
    if roll >= 4:
        print("You endure the storm and find the Sword!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The storm forces you back down.")
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
        print("The ghost smiles and grants you the Sword!")
        inventory.append("Sword of Power")
        return "sword"
    else:
        print("The ghost curses your journey.")
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
            print("The river sweeps you away.")
            return "failure"
    else:
        print("You avoid the river, but miss the sword.")
        return "failure"

def ending(result, name):
    print("\nThe monster attacks the capital!")
    if result == "sword":
        print(f"{name} wields the Sword of Power. Victory!")
    elif result == "cursed":
        print(f"{name} defeats the monster but vanishes into legend...")
    else:
        print(f"{name} fights bravely, but without the sword, the monster prevails...")

# ---------------- Run ----------------
if __name__ == "__main__":
    splash_screen()   # show sunset gradient first
    adventure()       # then start the interactive story
