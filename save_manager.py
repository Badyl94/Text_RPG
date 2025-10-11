import json

def save_game(game_state, filename="data/saves/save1.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(game_state.to_dict(), f, indent=4, ensure_ascii=False)

def load_game(filename="data/saves/save1.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    from game_state import GameState, Inventory
    state = GameState()
    state.player_name = data["player_name"]
    state.location = data["location"]
    state.inventory.quest_items = data["inventory"]["quest_items"]
    state.inventory.materials   = data["inventory"]["materials"]
    state.inventory.equipment   = data["inventory"]["equipment"]
    return state