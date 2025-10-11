import msvcrt
import time
import wood_chopping_minigame
import ops
import os
import sys
import monologues
import save_manager

def splash_screen():
    print("Welcome to the Text_RPG (all rights reserved)!!")
    input()
    os.system('cls')

def main_menu(game_state):
    os.system('cls')
    print("What would you like to do?\n"
          "1. Start a New Game\n"
          "2. Load Saved Game\n"
          "3. Exit")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'1':
               monologues.new_game_opening_section()
               monologues.character_creation(game_state)
            elif key == b'2':
                character_menu(save_manager.load_game())
            elif key == b'3':
                sys.exit()
            else:
                pass

def character_menu(game_state):
    os.system('cls')
    print("What do you want to do?")
    print("1. Check information about your character")
    print("2. Check your inventory")
    print("3. Chop wood")
    print("4. Save game")
    print("5. Go back to main menu")

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'1':
                game_state.show_summary()
                input("Press Enter to go back.")
                character_menu(game_state)
            elif key == b'2':
                game_state.inventory.show_inventory()
                input("Press Enter to go back.")
                character_menu(game_state)
            elif key == b'3':
                wood_to_be_added = wood_chopping_minigame.chopping_style_check()
                game_state.inventory.add_item("materials", "Wood", wood_to_be_added)
                input("Press Enter to continue.") 
                character_menu(game_state)
            elif key == b'4':
                filename = input("Provide a name for your save file: \n")
                save_manager.save_game(game_state, filename)
                print("Game saved successfully.")
                input("Press Enter to continue.")
                character_menu(game_state)
            elif key == b'5':
                main_menu(game_state)
        time.sleep(0.05)
