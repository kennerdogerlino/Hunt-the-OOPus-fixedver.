"""Ken Quisquino"""
import os
from area import Area
from character import Guide, angy_gnome, Giant_bat

# === Game State ===
PLAYER_LEVEL = 1
FOREST_COMPLETED = False
JUNGLE_COMPLETED = False
SKYLANDS_COMPLETED = False
CRIMSON_COMPLETED = False

BOW_OBTAINED = False
MIMIC_DEFEATED = False
DEAD = False

inventory = []

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def check_level_progression():
    global PLAYER_LEVEL
    if FOREST_COMPLETED and PLAYER_LEVEL == 1:
        PLAYER_LEVEL = 2
        print("Jungle Biome unlocked!")
    elif JUNGLE_COMPLETED and PLAYER_LEVEL == 2:
        PLAYER_LEVEL = 3
        print("Skylands Biome unlocked!")
    elif SKYLANDS_COMPLETED and PLAYER_LEVEL == 3:
        PLAYER_LEVEL = 4
        print("Crimson Biome unlocked!")
    elif CRIMSON_COMPLETED and PLAYER_LEVEL == 4:
        PLAYER_LEVEL = 5
        print("All levels completed!")
    input("Press Enter to continue...")

# === Area Setup ===
Wooden_house = Area("Wooden House")
Forest_entrance = Area("Forest Entrance")
Giant_Living_Tree = Area("Giant Tree")
Platforms = Area("Platforms")
Abandoned_room = Area("Abandoned Room")

Jungle_Biome_entrance = Area("Jungle Biome Entrance")
Jungle_ravine = Area("Jungle Ravine")
Vine_covered_wall = Area("Vine Covered Wall")
Wrong_room = Area("?? CHEST ??")
Correct_room = Area("Correct room")
Giant_rainforest = Area("Giant Rainforest")
A_frayed_knot = Area("A frayed-knot")
Jungle_shrine = Area("Jungle Shrine")

Sky_Island_entrance = Area("Sky Island")
Giant_Jaycee = Area("Giant the OBESE Giant")
Skyland_house = Area("Skyland House")
Two_MASSIVE_Gates = Area("Two MASSIVE Gates")
Goblin_Gang = Area("Goblin Gang")
Hog_Rider = Area("HOG RIIIDAAAAAAHHH")
Gooey_Golem = Area("Gooey Golem")
Skeleton_Army = Area("Skeleton Army")
Peka = Area("P.E.K.A")
Sneaky_Rock_Golem = Area("Sneaky Rock Golem")
A_massiver_gate = Area("A MASSIVER GATE")
Betsy = Area("BETSY THE MASSIVE OF MASSIVENESS")

Crimson_Biome_entrance = Area("Crimson Biome")
Prime_yogandog = Area("Prime Yogandog (All Seeing)")

# === Linking Areas ===
Wooden_house.link_areas(Sky_Island_entrance, "North")
Wooden_house.link_areas(Forest_entrance, "East")
Wooden_house.link_areas(Crimson_Biome_entrance, "South")
Wooden_house.link_areas(Jungle_Biome_entrance, "West")

Forest_entrance.link_areas(Wooden_house, "West")
Forest_entrance.link_areas(Giant_Living_Tree, "East")
Giant_Living_Tree.link_areas(Forest_entrance, "West")
Giant_Living_Tree.link_areas(Platforms, "South")
Platforms.link_areas(Abandoned_room, "South")

Jungle_Biome_entrance.link_areas(Wooden_house, "East")
Jungle_Biome_entrance.link_areas(Jungle_ravine, "West")
Jungle_ravine.link_areas(Jungle_Biome_entrance, "East")
Jungle_ravine.link_areas(Vine_covered_wall, "South")
Vine_covered_wall.link_areas(Jungle_ravine, "North")
Vine_covered_wall.link_areas(Wrong_room, "West")
Vine_covered_wall.link_areas(Correct_room, "South")
Jungle_ravine.link_areas(Giant_rainforest, "West")
Giant_rainforest.link_areas(Jungle_ravine, "East")
Giant_rainforest.link_areas(A_frayed_knot, "West")
A_frayed_knot.link_areas(Giant_rainforest, "East")
A_frayed_knot.link_areas(Jungle_shrine, "North")

Sky_Island_entrance.link_areas(Wooden_house, "South")
Sky_Island_entrance.link_areas(Giant_Jaycee, "North")
Giant_Jaycee.link_areas(Sky_Island_entrance, "South")
Giant_Jaycee.link_areas(Skyland_house, "North")
Skyland_house.link_areas(Giant_Jaycee, "South")
Skyland_house.link_areas(Two_MASSIVE_Gates, "North")
Two_MASSIVE_Gates.link_areas(Skyland_house, "South")
Two_MASSIVE_Gates.link_areas(Goblin_Gang, "West")
Two_MASSIVE_Gates.link_areas(Skeleton_Army, "East")
Goblin_Gang.link_areas(Two_MASSIVE_Gates, "East")
Goblin_Gang.link_areas(Hog_Rider, "North")
Hog_Rider.link_areas(Goblin_Gang, "South")
Hog_Rider.link_areas(Gooey_Golem, "North")
Gooey_Golem.link_areas(Hog_Rider, "South")
Gooey_Golem.link_areas(A_massiver_gate, "East")
Skeleton_Army.link_areas(Two_MASSIVE_Gates, "West")
Skeleton_Army.link_areas(Peka, "North")
Peka.link_areas(Skeleton_Army, "South")
Peka.link_areas(Sneaky_Rock_Golem, "North")
Sneaky_Rock_Golem.link_areas(Peka, "South")
Sneaky_Rock_Golem.link_areas(A_massiver_gate, "West")
A_massiver_gate.link_areas(Gooey_Golem, "West")
A_massiver_gate.link_areas(Sneaky_Rock_Golem, "East")
A_massiver_gate.link_areas(Betsy, "North")
Betsy.link_areas(A_massiver_gate, "South")

Crimson_Biome_entrance.link_areas(Prime_yogandog, "South")
Prime_yogandog.link_areas(Crimson_Biome_entrance, "North")

# === NPCs ===
guide = Guide("Jaycee", "Your definitely-helpful-but-sigma guide.")
Wooden_house.set_character(guide)

gnome = angy_gnome()
Platforms.set_character(gnome)

Giant_rainforest.set_character(Giant_bat)

current_area = Wooden_house

print("Welcome to Hunt the OOPus")
print("Type directions like 'North', 'South' (or just N, E, S, W), or 'spawn' to return to Wooden House.")

direction_map = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
}

# === Game Loop ===
while not DEAD:
    clear_console()

    # === Biome Completion ===
    if current_area == Abandoned_room and not FOREST_COMPLETED:
        FOREST_COMPLETED = True
        inventory.append("Copper Sword")
        print("Forest Biome complete! You received the ✨⚔️  Golden Sword!")
        input("Press Enter to continue...")

    if current_area == Giant_rainforest and not JUNGLE_COMPLETED and BOW_OBTAINED:
        JUNGLE_COMPLETED = True
        print("Jungle Biome complete!")
        input("Press Enter to continue...")

    if current_area == Betsy and not SKYLANDS_COMPLETED:
        SKYLANDS_COMPLETED = True
        print("Skylands Biome complete!")
        input("Press Enter to continue...")

    if current_area == Prime_yogandog and not CRIMSON_COMPLETED:
        CRIMSON_COMPLETED = True
        print("Crimson Biome complete!")
        input("Press Enter to continue...")

    check_level_progression()

    print(f"\nYou are in: {current_area.name}")
    current_area.get_details()

    # === Hermit Encounter ===
    if current_area == Vine_covered_wall and not BOW_OBTAINED:
        print("🧙‍♂️ A mysterious Hermit blocks the doors from WEST and SOUTH...")
        print("He whisperinationisms: 'One door holds death. The other... well, uhhhhhh. Not death. EZ games. in my language, we call this, fortnite battle pass scenario'")
        door_choice = input("Enter direction ('West' or 'South'): ").lower()
        if door_choice in ["west", "w"]:
            current_area = Wrong_room
        elif door_choice in ["south", "s"]:
            if MIMIC_DEFEATED:
                current_area = Correct_room
            else:
                print("The Hermit says: 'Face the mimic first, or be cursed forever.'")
                input("Press Enter to continue...")
                continue

    # === Mimic Battle ===
    if current_area == Wrong_room and not MIMIC_DEFEATED:
        print("A treasure chest reveals TEETH—it's the Mimic!")
        fight = input("Fight it? (yes/no): ").lower()
        if fight == "yes":
            weapon = input("What weapon do you use?: ").lower()
            if weapon in [item.lower() for item in inventory]:
                print("You slay the Mimic in a shower of jungle guts!")
                MIMIC_DEFEATED = True
                current_area = Vine_covered_wall
            else:
                print("You lack the weapon. The Mimic devours you whole.")
                DEAD = True
        else:
            print("You flee from the chest back to the Hermit...")
            current_area = Vine_covered_wall
            input("Press Enter to continue...")
            continue

    # === Reward Room ===
    if current_area == Correct_room and not BOW_OBTAINED:
        print("🏹 You discover the legendary Bow and Arrow!")
        inventory.append("Bow and Arrow")
        BOW_OBTAINED = True
        print("Return to the Jungle Ravine to continue...")
        input("Press Enter to continue...")

    # === NPCs & Combat ===
    character = current_area.get_character()
    if character:
        character.describe()
        if isinstance(character, Guide):
            character.interact()
        elif isinstance(character, angy_gnome):
            print("The Angy Gnome barks at you!")
            fight = input("Do you fight him? (yes/no): ").lower()
            if fight == "yes":
                weapon = input("What weapon do you use?: ").lower()
                if weapon == "copper sword" or "fortnite dance moves" and any(item.lower() == "copper sword" for item in inventory):
                    print("You struck the gnome’s weakness! He cooketh foreals.")
                    current_area.set_character(None)
                elif weapon in [item.lower() for item in inventory]:
                    print("You defeated the gnome!")
                    current_area.set_character(None)
                else:
                    print("You lost the fight.")
                    DEAD = True

    # === Navigation ===
    command = input("\nDirection? (N, E, S, W or 'spawn'): ").lower()

    if command == "spawn":
        current_area = Wooden_house
        print("Returning to Wooden House...")

    elif command == "inventory":
        print("\nInventory:")
        if inventory:
            for item in inventory:
                print(f" - {item}")
        else:
            print(" (empty)")
        input("Press Enter to continue...")

    elif command in direction_map:
        direction = direction_map[command]
        next_area = current_area.linked_areas.get(direction)

        if next_area:
            # Level gating logic
            if next_area in [Jungle_Biome_entrance, Jungle_ravine, Vine_covered_wall, Giant_rainforest] and PLAYER_LEVEL < 2:
                print("You must complete Level 1 first.")
                input("Press Enter to continue...")
                continue
            elif next_area in [Sky_Island_entrance, Giant_Jaycee, Skyland_house, Two_MASSIVE_Gates,
                               Goblin_Gang, Hog_Rider, Gooey_Golem, Skeleton_Army, Peka,
                               Sneaky_Rock_Golem, A_massiver_gate, Betsy] and PLAYER_LEVEL < 3:
                print("You must complete Level 2 first.")
                input("Press Enter to continue...")
                continue
            elif next_area in [Crimson_Biome_entrance, Prime_yogandog] and PLAYER_LEVEL < 4:
                print("You must complete Level 3 first.")
                input("Press Enter to continue...")
                continue

            if current_area.name == "Platforms" and direction == "South":
                if Platforms.get_character():
                    print("The Angy Gnome blocks your path!")
                    input("Press Enter to continue...")
                    continue

            current_area = next_area
        else:
            print("You can’t go that way.")
            input("Press Enter to continue...")

    else:
        print("Invalid command.")
        input("Press Enter to continue...")
