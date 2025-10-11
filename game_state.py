from typing import Dict

class Inventory:
    def __init__(self):
        self.quest_items: Dict[str, int] = {}
        self.materials:   Dict[str, int] = {}
        self.equipment:   Dict[str, int] = {}

    def add_item(self, category: str, name: str, amount: int = 1):
        target = getattr(self, category)
        target[name] = target.get(name, 0) + amount

    def to_dict(self):
        return {
            "quest_items": dict(self.quest_items),
            "materials": dict(self.materials),
            "equipment": dict(self.equipment)
        }

class GameState:
    def __init__(self):
        self.inventory = Inventory()
        self.player_name = "Unknown Name"
        self.player_gender = "Unknown Gender"
        self.player_profession = "Unknown Profession"
        self.player_level = 1
        self.player_location = "Broken Hopes Canyon"
        self.current_experience = 0
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
            "location": self.location,
            "inventory": self.inventory.to_dict()
        }
    def show_summary(self):
        print("\n=== PLAYER SUMMARY ===")
        print(f"Name:       {self.player_name}")
        print(f"Gender:     {self.player_gender}")
        print(f"Profession: {self.player_profession}")
        print(f"Location:   {self.player_location}")
        print("======================\n")