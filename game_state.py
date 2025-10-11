from typing import Dict

class Inventory:
    def __init__(self):
        self.quest_items: Dict[str, int] = {}
        self.materials:   Dict[str, int] = {}
        self.equipment:   Dict[str, int] = {}

    def add_item(self, category: str, name: str, amount: int = 1):
        target = getattr(self, category)
        if name not in target:
            target[name] = 0
        target[name] = target.get(name, 0) + int(amount)

    def to_dict(self):
        return {
            "quest_items": dict(self.quest_items),
            "materials": dict(self.materials),
            "equipment": dict(self.equipment)
        }
    def show_inventory(self):
        print("\n=== INVENTORY ===")

        if not any([self.quest_items, self.materials, self.equipment]):
            print("Your inventory is empty.")
        else:
            print("\n-- Quest Items --")
            if self.quest_items:
                for item, amount in self.quest_items.items():
                    print(f"{item}: {amount}")
            else:
                print("None")

            print("\n-- Materials --")
            if self.materials:
                for item, amount in self.materials.items():
                    print(f"{item}: {amount}")
            else:
                print("None")

            print("\n-- Equipment --")
            if self.equipment:
                for item, amount in self.equipment.items():
                    print(f"{item}: {amount}")
            else:
                print("None")

        print("=================\n")
        
class GameState:
    def __init__(self):
        self.inventory = Inventory()
        self.player_name = "Unknown Name"
        self.player_gender = "Unknown Gender"
        self.player_profession = "Unknown Profession"
        self.player_level = 1
        self.player_location = "Broken Hopes Canyon"
        self.player_experience = 0
        # Future: missions? stats?

    def set_player(self, name=None, gender=None, profession=None):
        if name is not None:
            self.player_name = name
        if gender is not None:
            self.player_gender = gender
        if profession is not None:
            self.player_profession = profession

    def to_dict(self):
        return {
            "player_name": self.player_name,
            "player_gender": self.player_gender,
            "player_location": self.player_location,
            "player_profession": self.player_profession,
            "player_level": self.player_level,
            "player_experience": self.player_experience,
            "inventory": self.inventory.to_dict()
        }
    def show_summary(self):
        print("\n=== PLAYER SUMMARY ===")
        print(f"Name:       {self.player_name}")
        print(f"Gender:     {self.player_gender}")
        print(f"Profession: {self.player_profession}")
        print(f"Location:   {self.player_location}")
        print("======================\n")

    