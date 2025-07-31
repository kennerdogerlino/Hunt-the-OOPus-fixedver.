import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

class Character:
    """Defines attributes and methods for Character objects"""
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} has appeared.")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says: {self.conversation}")
        else:
            print(f"{self.name} does not want to talk to you.")

    def fight(self, combat_item):
        print(f"{self.name} does not want to fight with you.")
        return True

class Enemy(Character):
    """Enemy subclass of Character with combat functionality"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        # Normalize the weakness string
        self.weakness = item_weakness.lower().strip()

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        # Normalize combat item before comparison
        normalized_item = combat_item.lower().strip()
        if normalized_item == self.weakness:
            print(f"\nYou fend off {self.name} with the {combat_item}.")
            return True
        else:
            print(f"{self.name} just owned you. You are defeated!")
            return False

class Guide(Character):
    """Guide character with interaction options"""
    def __init__(self, name, description):
        super().__init__(name, description)

    def describe(self):
        print(f"{self.name} is here. {self.description}")

    def interact(self):
        print("\nEnter 'I' to interact with the guide.")
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
        
        choice = input("Choose option (1, 2, or leave): ").lower().strip()

        if choice == "1":
            print("JAYCEE: So... You've finally woken up.")
            print("It's a world of danger. Biomes lie in all directions.")
            print("I gave you a copper sword to begin your journey.")
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
        next_action = input("> ").lower().strip()

        if next_action == "hint":
            print("JAYCEE whispers: 'The forest to the East will be the first area to explore. Head there to begin your journey.'")
        elif next_action == "e":
            print("JAYCEE smirks: 'Good luck out there...'")
        else:
            print("JAYCEE: If you're confused, just explore. You'll be fine... I think.")

class angy_gnome(Enemy):
    """Angy Gnome enemy with specific weakness"""
    def __init__(self):
        super().__init__(
            "Angy Gnome",
            "A very aggressive but teeny weeny gnome with rage issues, crashing out over touching grass.")
        self.set_weakness("copper sword")
        self.set_weakness("fortnite dance moves")

    def describe(self):
        print(f"{self.name} snarls at you angrily!")

class Giant_bat(Enemy):
    """A massive bat that can only be defeated with a bow and arrow."""
    def __init__(self):
        super().__init__(
            "Giant Bat",
            "A monstrous bat swoops above with razor wings. Only a well-aimed arrow can bring it down."
        )
        self.set_weakness("bow and arrow")

    def describe(self):
        print(f"{self.name} shrieks from above, its wings blotting out the canopy!")

    def fight(self, combat_item):
        normalized_item = combat_item.lower().strip()
        if normalized_item == self.weakness:
            print(f"\nYour arrow slices through the air and strikes true. {self.name} crashes into the treetops!")
            return True
        else:
            print(f"\nYou try to fight with the {combat_item}, but the Giant Bat grabs you mid-air...")
            print("Your body locks up in eternal immobilization as its venom takes hold.")
            return False

