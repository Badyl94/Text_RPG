import wood_chopping_minigame
import ops
import menus
import monologues
import pygame
import os
from game_state import GameState

# pygame.mixer.init()
# pygame.mixer.music.load("audio/music/main_music.mp3")
# pygame.mixer.music.play(-1) 

def main():
    game_state = GameState()
    os.system('cls')
    menus.splash_screen()
    menus.main_menu(game_state)

main()

#pygame.mixer.music.stop()