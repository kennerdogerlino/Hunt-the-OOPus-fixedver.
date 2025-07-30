"""its a Area class"""
class Area:
    """Defines attributes and methods for area objects"""
    def __init__(self, area_name):
        """Sets class attributes"""
        self.name = area_name
        self.description = None
        self.linked_areas = {}
        self.character = None
        self.items = []

    def set_name(self, area_name):
        """Sets the area name"""
        self.name = area_name

    def get_name(self):
        """Gets the area name"""
        return self.name

    def set_description(self, area_description):
        """Sets the area description"""
        self.description = area_description

    def get_description(self):
        """Gets the area description"""
        return self.description

    def describe(self):
        """Prints the area's description"""
        print(self.description)

    def link_areas(self, area_to_link, direction):
        """Populates dictionary of linked area"""
        self.linked_areas[direction] = area_to_link
        #print(self.name + "linked areas:" + repr(self.linked_areas))

    def get_details(self):
        print(f"== {self.name} ==")
        for direction, area in self.linked_areas.items():
            print(f"{direction}: {area.name}")
        if self.items:
            print("You see the following items here:")
            for item in self.items:
                print(f" - {item}")

    def move(self, direction):
        """moves to different area's depends on direction"""
        if direction in self.linked_areas:
            return self.linked_areas[direction]
        else:
            print("You dingus, can't go that way bro")
            return self

    def set_character(self, new_character):
        """Sets character"""
        self.character = new_character

    def get_character(self):
        """Returns the name of the character object in this area"""
        return self.character

    def add_item(self, item):
        if item in self.items:
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)