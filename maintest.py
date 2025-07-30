"""Ken Quisquino"""
import os
from area import Area
from character import Guide, angy_gnome

# === Level tracking ===
PLAYER_LEVEL = 1
FOREST_COMPLETED = False
JUNGLE_COMPLETED = False
SKYLANDS_COMPLETED = False
CRIMSON_COMPLETED = False

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# === Area Setup ===
Wooden_house = Area("Wooden House")
Forest_entrance = Area("Forest Entrance")
Giant_Living_Tree = Area("Giant Tree")
Platforms = Area("Platforms")
Abandoned_Room = Area("Abandoned Room")
Jungle_Biome_entrance = Area("Jungle Biome Entrance")
Jungle_ravine = Area("Jungle Ravine")
Vine_covered_wall = Area("Vine Covered Wall")
Rainforest = Area("Rainforest")
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
Platforms.link_areas(Abandoned_Room, "South")

Jungle_Biome_entrance.link_areas(Wooden_house, "East")
Jungle_Biome_entrance.link_areas(Jungle_ravine, "West")
Jungle_ravine.link_areas(Jungle_Biome_entrance, "East")
Jungle_ravine.link_areas(Vine_covered_wall, "South")
Jungle_ravine.link_areas(Rainforest, "West")
Rainforest.link_areas(Jungle_ravine, "East")

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

# === NPCs & Enemies ===
guide = Guide("Jaycee", "Your definitely-helpful-but-sigma guide.")
Wooden_house.set_character(guide)

gnome = angy_gnome()
Platforms.set_character(gnome)

# === Game Loop ===
current_area = Wooden_house
DEAD = False

print("Welcome to Hunt the OOPus")
print("Type directions like 'North', 'South' (N, E, S, W), or 'spawn' to return to Wooden House.")

while not DEAD:
    clear_console()
    print(f"\nYou are now in: 🧭 {current_area.name} 🧭")
    current_area.get_details()


    inhabitant = current_area.get_character()
    if inhabitant:
        inhabitant.describe()

        if isinstance(inhabitant, Guide):
            inhabitant.interact()

        elif isinstance(inhabitant, angy_gnome):
            print("You see the Angy Gnome snarling at you!")
            action = input("Do you fight him? (y/n): ").lower()
            if action == "yes":
                weapon = input("What weapon do you use?: ").lower()
                if inhabitant.fight(weapon):
                    print("You defeated the gnome!")
                    current_area.set_character(None)
                else:
                    DEAD = True
                    continue

    command = input("\nDirection? (enter 'North, East, South, West' or or 'spawn'): ").capitalize()

    direction_map = {
        "n":"North",
        "e":"East",
        "s":"South",
        "w":"West",
    }

    if command == "Spawn":
        clear_console()
        current_area = Wooden_house
        print("Respawned in Wooden House.")

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

    elif command in ["North", "South", "East", "West"]:
        next_area = current_area.linked_areas.get(command)

        if next_area:
            # Level gating
            if next_area in [Jungle_Biome_entrance, Jungle_ravine, Vine_covered_wall, Rainforest] and PLAYER_LEVEL < 2:
                print("🔒 You must complete Level 1 first. 🔒")
            elif next_area in [Sky_Island_entrance, Giant_Jaycee, Skyland_house, Two_MASSIVE_Gates,
                            Goblin_Gang, Hog_Rider, Gooey_Golem, Skeleton_Army, Peka, Sneaky_Rock_Golem,
                            A_massiver_gate, Betsy] and PLAYER_LEVEL < 3:
                print("🔒 You must complete Level 2 first. 🔒")
            elif next_area in [Crimson_Biome_entrance, Prime_yogandog] and PLAYER_LEVEL < 4:
                print("🔒 You must complete Level 3 first. 🔒")
            else:
                current_area = next_area
                clear_console()
        else:
            print("There's nothing there, bruh.")

    else:
        print("That ain't a command dingus. Try North, East, South, West or Spawn.")

else:
    print("That ain't a command dingus. Try North, East, South, West or Spawn.")

    # Completion triggers
    if current_area == Abandoned_Room and not FOREST_COMPLETED:
        clear_console
        print("🎉 Forest Biome complete!")
        FOREST_COMPLETED = True

    if current_area == Rainforest and not JUNGLE_COMPLETED:
        clear_console
        print("🎉 Jungle Biome complete!")
        JUNGLE_COMPLETED = True

    #if current_area == Betsy and not SKYLANDS_COMPLETED:
    #print("🎉 Skylands Biome complete!")
    #SKYLANDS_COMPLETED = True