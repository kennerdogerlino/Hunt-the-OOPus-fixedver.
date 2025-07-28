"""Character class for Hunt the OOPus"""
class Character:
    """Defines attributes and methods for Character objects"""
    def __init__(self, char_name, char_description):
        """Sets the class attributes"""    
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Gives the characters a description"""
        print(self.name + " has returned!")
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

class Guide(Character):
    def __init__(char_name, char_description):

    #def help():
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
            