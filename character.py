"""Character class for Hunt the OOPus"""
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

class Character:
    """Defines attributes and methods for Character objects"""
    def __init__(self, char_name, char_description):
        """Sets the class attributes"""    
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Gives the characters a description"""
        print(self.name + " Jaycee has appeared")
        print(self.description)

    def set_conversation(self, conversation):
        """Sets what the character can say"""
        self.conversation = conversation

    def talk(self):
        """Allows characters to talk to player"""
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " does not want to talk to you.")

    def fight(self):
        """Allows characters to fight with the player"""
        print(self.name + " doe not want to fight with you.")
        return True

class Enemy(Character):
    """Creates enemey class"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None #he dont even go to school no more.

    def set_weakness(self, item_weakness):
        """Sets enemy weakness"""
        self.weakness = item_weakness

    def get_weakness(self):
        """Gets enemy weakness"""
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("\nYou fend off " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " swallows you whole! You died.")

    def help():
        """prints hints after each level"""

class TreasureChest():
    def __init__(self, chest_name):
        self.chest_name = chest_name
        self._valuable = []
        self._owner = None
        self.is_locked = True

    def set_owner(self, owner_name):
        self.owner = owner_name
        print(f"{self.chest_name} is now reserved for {owner_name}.")

    def add_valuable(self, item):
        self.valuables.append(item)
        print(f"{self.chest_name} has been added to {self.chest_name}.")

    def retrive_valuable(self, item):
        if not self.is_locked:
            print(f"You find: {', '.join(self._valuables) if self._valuables else 'nothing... it’s empty!'}")
            self._valuables.clear()
        else:
            print("The chest is locked. You need permission to open it.")

class Guide(Character):
    def __init__(self, name, description): 
        self.name = name
        self.description = description

    def describe(self):
        print(f"{self.name} is here. {self.description}")

    def interact(self):
        print("\nEnter I to interact with the guide")
        key = input("> ").upper()

        if key == "I":
            self.show_dialogue()
        else:
            print("You decide not to interact with the guide.")

    def show_dialogue(self):
        clear_console()
        print("\n*** JAYCEE THE GUIDE INTERACTION ***")
        print("1. Where am I?")
        print("2. What place is this?")
        print("Type 'leave' to exit the conversation.")
        
        choice = input("Choose option (1, 2, or leave): ").upper()

        if choice == "1":
            print("JAYCEE: So... You've finally woken up.")
            print("It's a world of danger. Biomes lie in all directions.")
        elif choice == "2":
            print("JAYCEE: You're in my Wooden House, your spawn point.")
            print("I gave you my copper sword.")
            print("You can return here if you're defeated or by typing 'spawn'.")
        elif choice == "leave":
            print("You left the conversation.")
            return
        else:
            print("JAYCEE: I don't understand what you're asking.")

        self.show_hint()

    def show_hint(self):
        print("\nType 'hint' for a clue, or press 'E' to exit and continue your journey.")
        next_action = input("> ").upper()

        if next_action == "hint":
            print("JAYCEE whispers: 'The forest to the East will be the first area to explore. Head there to begin your journey.'")
        elif next_action == "e":
            print("JAYCEE smirks creepily: 'Good luck out there...'")
        else:
            print("JAYCEE: If you're confused, just explore. You be fine... I think")

class angy_gnome(Enemy):
    def __init__(self):
        super().__init__(
            "Angy Gnome", 
            "A very-way-too-agressive-but-insanely-small gnome with rage issues")
        self.set_weakness("copper sword")
        