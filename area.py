class Area:
    def __init__(self, area_name):
        self.name = area_name
        self.description = None
        self.linked_areas = {}
        self.character = None

    def set_name(self, area_name):
        self.name = area_name

    def get_name(self):
        return self.name

    def set_description(self, area_description):
        self.description = area_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def link_areas(self, area_to_link, direction):
        self.linked_areas[direction] = area_to_link

    def get_details(self):
        print(f"== {self.name} ==")
        for direction, area in self.linked_areas.items():
            print(f"{direction}: {area.name}")

    def move(self, direction):
        if direction in self.linked_areas:
            return self.linked_areas[direction]
        else:
            print("You can't go that way.")
            return self

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
