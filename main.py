"""Imports cave to Area"""
import os
from area import Area
from character import Enemy, Character, Guide
from datetime import datetime

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



current_area = Wooden_house
DEAD = False
while DEAD is not False:
    print("\n")
    current_area.get_details()
    inhabitated = current_area.get_character()
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ")
    if command in ["North", "East", "South", "West"]:
        current_area = current_area.move(command)
    elif command == "Talk":
        if inhabitated is not None:
            inhabitated.talk()
    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What you fight with cuh? ")
            if inhabitated.fight(fight_with) is True:
                print("W's in the chat! You win the battle")
            else:
                print("Flabbergastinations! You lost the fight.")
                DEAD = True
        else:
            print("There is no one here to fight with")
