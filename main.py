"""Imports cave to Area"""
import os
from area import Area
from character import Enemy, Character, Guide, angy_gnome

#sigma level tracking
PLAYER_LEVEL = 1
FOREST_COMPLETED = False
JUNGLE_COMPLETED = False
SKYLANDS_COMPLETED = False
CRIMSON_COMPLETE = False

def clear_console():
    """Clears the console in terminal"""
    os.system("cls" if os.name == "nt" else "clear")

#Spawnpoint (can respawn when dead)
Wooden_house = Area("Wooden House")

#Level 1 forest biome section
Forest_entrance = Area("forest entrance")
Giant_Living_Tree = Area("Giant Tree")
Platforms = Area("Platforms")
Abandoned_Room  = Area("Abandoned room")

#Level 2 Jungle Biome section
Jungle_Biome_entrance = Area("Wooden House")
Jungle_ravine = Area("Wooden House")

#South/down direction from jungle ravine
Vine_covered_wall = Area("Vine covered wall")
GOLDEN_CHEST = Area("???GOLDEN CHEST???")
Golden_chest = Area("Golden Chest!")

#West direction going past ravine
Rainforest = Area("Rainforest")

#Level 3 Sky Island Biome section
Giant_Jaycee = Area("Jaycee the OBESE Giant")
Sky_Island_entrance = Area("Sky Island")
Skyland_house = Area("Skyland House")
Two_MASSIVE_Gates = Area("2 MASSIVE gates")
Goblin_Gang = Area("Goblin gang")
Hog_Rider = Area("HOG RIIIDAAAAAAHHH")
Gooey_Golem = Area("Gooey Golem")
Skeleton_Army = Area("Skeleton army")
Peka = Area("P.E.K.A")
Sneaky_Rock_Golem = Area("Sneaky Golem in the pocket")
A_massiver_gate = Area("A MASSIVER GATE")
Betsy_The_Massive_Of_Massiveness = Area("BETSY THE MASSIVE OF MASSIVENESS")


#Level 4 Crimson Biome section
Crimson_Biome_entrance = Area("Crimson Biome")
Prime_yogandog = Area ("Prime Yogandog (All seeing)")

#Link_areas
Wooden_house.link_areas(Sky_Island_entrance, "North")
Wooden_house.link_areas(Forest_entrance, "East")
Wooden_house.link_areas(Crimson_Biome_entrance, "South")
Wooden_house.link_areas(Jungle_Biome_entrance, "West")

Forest_entrance.link_areas(Wooden_house, "West")
Forest_entrance.link_areas(Giant_Living_Tree, "East")
Giant_Living_Tree.link_areas(Platforms, "South")
Giant_Living_Tree.link_areas(Forest_entrance, "West")
Platforms.link_areas(Abandoned_Room, "South")

Jungle_Biome_entrance.link_areas(Wooden_house, "East")
Jungle_Biome_entrance.link_areas(Jungle_ravine, "West")
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
A_massiver_gate.link_areas(Betsy_The_Massive_Of_Massiveness, "North")
Betsy_The_Massive_Of_Massiveness.link_areas(A_massiver_gate, "South")

Crimson_Biome_entrance.link_areas(Prime_yogandog, "South")
Prime_yogandog.link_areas(Crimson_Biome_entrance, "North")

#NPC peepul:
JAYCEE = Guide
Wooden_house.set_character(JAYCEE)

#enemy classes
Angy_Gnome = angy_gnome

def setup_game():
    """Sets the game, where you always spawn"""
    Wooden_house = Area("Wooden House")
    Forest_entrance = Area("Forest Entrance")


    Wooden_house.link_areas(Sky_Island_entrance, "North")
    Wooden_house.link_areas(Forest_entrance, "East")
    Wooden_house.link_areas(Crimson_Biome_entrance, "South")
    Wooden_house.link_areas(Jungle_Biome_entrance, "West")

    JAYCEE = Guide("JAYCEE, your definitly-helpful-but-sigma guide.")
    Wooden_house.set_character(JAYCEE)

    return Wooden_house

def main():
    global PLAYER_LEVEL, FOREST_COMPLETED, JUNGLE_COMPLETED, SKYLANDS_COMPLETED, CRIMSON_COMPLETED

    current_area = Wooden_house
    DEAD = False

    print("Welcome to Hunt the OOPus")
    print("Type directions like 'North', 'South', or type 'spawn' to return to Wooden House.")

    while not DEAD:
        print(f"\nYou are now in: {current_area.name}")
        command = input("What do you want to do? ")

        if command.lower() == "spawn":
            current_area = Wooden_house
            print("You returned to Wooden House.")

            # Level progression unlocks
            if FOREST_COMPLETED and PLAYER_LEVEL == 1:
                PLAYER_LEVEL = 2
                print("🌿 Level 2 (Jungle Biome) is now unlocked!")

            elif JUNGLE_COMPLETED and PLAYER_LEVEL == 2:
                PLAYER_LEVEL = 3
                print("☁️ Level 3 (Skylands Biome) is now unlocked!")

            elif SKYLANDS_COMPLETED and PLAYER_LEVEL == 3:
                PLAYER_LEVEL = 4
                print("🩸 Level 4 (Crimson Biome) is now unlocked!")

            elif CRIMSON_COMPLETED and PLAYER_LEVEL == 4:
                PLAYER_LEVEL = 5
                print("🎉 You've completed all levels!")

        elif command in ["North", "South", "East", "West"]:
            next_area = current_area.linked_areas.get(command)

            if not next_area:
                print("You can't go that way.")
                continue

            # Gated biome access by level
            if next_area in [Jungle_Biome_entrance, Jungle_ravine, Vine_covered_wall, Rainforest] and PLAYER_LEVEL < 2:
                print("requirements: area level 1 must be completed first")
                continue

            elif next_area in [Sky_Island_entrance, Giant_Jaycee, Skyland_house, Two_MASSIVE_Gates,
                               Goblin_Gang, Hog_Rider, Gooey_Golem, Skeleton_Army, Peka, Sneaky_Rock_Golem,
                               A_massiver_gate, Betsy_The_Massive_Of_Massiveness] and PLAYER_LEVEL < 3:
                print("requirements: area level 2 must be completed first")
                continue

            elif next_area in [Crimson_Biome_entrance, Prime_yogandog] and PLAYER_LEVEL < 4:
                print("requirements: area level 3 must be completed first")
                continue

            else:
                current_area = next_area

        # === Check for biome completions ===
        if current_area == Abandoned_Room and not FOREST_COMPLETED:
            print("✅ You have completed the Forest biome (Level 1)!")
            print("Type 'spawn' to return to Wooden House and unlock the next level.")
            FOREST_COMPLETED = True

        if current_area == Rainforest and not JUNGLE_COMPLETED:
            print("✅ You have completed the Jungle biome (Level 2)!")
            print("Type 'spawn' to return to Wooden House and unlock the next level.")
            JUNGLE_COMPLETED = True

        if current_area == Betsy_The_Massive_Of_Massiveness and not SKYLANDS_COMPLETED:
            print("✅ You have completed the Skylands biome (Level 3)!")
            print("Type 'spawn' to return to Wooden House and unlock the next level.")
            SKYLANDS_COMPLETED = True


