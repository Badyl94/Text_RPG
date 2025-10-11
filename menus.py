import msvcrt
import time
import wood_chopping_minigame
import ops
import os
import sys
import monologues


def splash_screen():
    print("Welcome to the Text_RPG (all rights reserved)!!")
    input()
    os.system('cls')

def main_menu(game_state):
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
                load_game()
                pass
            elif key == b'3':
                sys.exit()
            else:
                pass

def character_menu(game_state):
    os.system('cls')
    #location name will be replaced
    #print(f"You are located in Broken Hopes Canyon")
    print("What do you want to do?")
    print("1. Check information about your character")
    print("2. Chop wood")
    print("3. Go back to main menu")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'1':
                game_state.show_summary()
                input("Press Enter to go back.")
                character_menu(game_state)
            elif key == b'2':
                wood_chopping_minigame.chopping_style_check()
            elif key == b'3':
                main_menu()
            else:
                print(f"Invalid key {key}. Press 1 or 2.")
        time.sleep(0.05)

def load_game():
    pass