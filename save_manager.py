import json
import os
import glob

def save_game(game_state, filename):
    filename = f"data/saves/{filename}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(game_state.to_dict(), f, indent=4, ensure_ascii=False)

def load_game():
    folder = "data/saves"
    files = glob.glob("data/saves/*.json")
    os.system('cls')
    print("List of your save files:")
    save_file_names = [os.path.splitext(os.path.basename(f))[0] for f in files]
    for name in save_file_names:
        print(name)
    filename = input("Please provide exact name of the file: \n")
    exact_filename = f"data/saves/{filename}.json"
    #filename example: filename="data/saves/save1.json"
    with open(exact_filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    from game_state import GameState, Inventory
    state = GameState()
    state.player_name = data["player_name"]
    state.player_gender = data["player_gender"]
    state.player_location = data["player_location"]
    state.player_profession = data["player_profession"]
    state.player_level = data["player_level"]
    state.player_experience = data["player_experience"]
    state.inventory.quest_items = data["inventory"]["quest_items"]
    state.inventory.materials   = data["inventory"]["materials"]
    state.inventory.equipment   = data["inventory"]["equipment"]
    return state