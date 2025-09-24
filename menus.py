import msvcrt
import time
import wood_chopping_minigame

def main_menu():
    # Start new game
    # Load game
    # Exit
    pass


def character_menu():
    print("What do you want to do?")
    print("1. Chop wood")
    print("2. Go back to main menu")
    #input()
    while True:  # ⬅️ ZMIANA: pętla oczekująca na wciśnięcie klawisza
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'1':
                wood_chopping_minigame.chopping_style_check()
            elif key == b'2':
                main_menu()  # kończymy funkcję
            else:
                print(f"Invalid key {key}. Press 1 or 2.")
        time.sleep(0.05)  # ⬅️ ZMIANA: mała pauza, żeby nie obciążać CPU