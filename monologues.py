import ops
import sys
import time
import os
import pygame
import msvcrt
import menus

def new_game_opening_section():
    #comment next 3 lines to not skip
    skip = input("Press Enter to skip intro") == ""
    if skip:
        return
    os.system('cls')
    ops.print_3_dots(1)
    msg1 = 'A long time ago in a galaxy far, far away'
    msg2 = '... no, wait...'
    ops.print_text(msg1,0.06)
    ops.print_3_dots(2)
    ops.print_text(msg2,0.1)
    ops.erase_text_len(len(msg1+msg2))
    msg1 = 'Once upon a time, in a land far, far away'
    msg2 = '... nah'
    ops.print_3_dots(2)
    ops.print_text(msg1,0.06)
    ops.print_3_dots(1)
    ops.print_text(msg2,0.06)
    ops.print_3_dots(1)
    ops.erase_text_len(len(msg1+msg2))
    ops.print_3_dots(2)
    ops.print_text("Well, anyway...\n",0.06)
    ops.print_3_dots(1)
    os.system('cls')
    ops.print_3_dots(1)
    ops.print_text("At some place you definitely haven't seen yet!\n",0.06)
    time.sleep(1)
    sys.stdout.write("                                               ")
    sys.stdout.flush()
    ops.print_text("In times you haven't heard about!\n",0.06)
    time.sleep(1)
    sys.stdout.write("       ")
    sys.stdout.flush()
    ops.print_text("To people you didn't even know existed!",0.06)
    time.sleep(1.5)
    os.system('cls') 
    # pygame.mixer.Sound("audio/sounds/thunder.mp3").play()
    time.sleep(0.1)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!...............!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    print("                                 STUFF HAPPENED!\n")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!...............!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(3)
    sys.stdout.write("\n\n\n               ")
    sys.stdout.flush()
    ops.print_text("And this is a story of a stuff doer and stuff witness!\n\n",0.06)
    time.sleep(5)

def character_creation(game_state):
    #comment next 6 lines to not skip
    skip = input("Press Enter to skip character creation") == ""
    if skip:
        game_state.set_player(gender='Man')
        game_state.set_player(name='Badyl')
        game_state.set_player(profession='Warrior')
        menus.character_menu(game_state)
    os.system('cls')
    ops.print_text("Oh... so you are alive indeed!\n",0.06)
    ops.print_text("It's good to see another...\n",0.06)
    print("1. Man")
    print("2. Woman")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'1':
                game_state.set_player(gender='Man')
                break
            elif key == b'2':
                game_state.set_player(gender='Woman')
                break
    ops.print_text(f"... {game_state.player_gender.lower()} who's not dead yet!\n",0.06)
    ops.print_text("Tell me, do you remember anything from your past?\n"
                   "What was your name?\n"
                   "What were you doing?\n"
                   "Anything really!\n",0.06)
    time.sleep(1)
    ops.print_3_dots(1)
    while True:
        name = input("~~I guess my name is... ").strip()
        if len(name) == 0:
            print("Name cannot be empty.")
        elif len(name) > 16:
            print("Name cannot be longer than 16 characters.")
        elif not name.isalpha():
            print("Name can only contain letters.")
        else:
            break

    game_state.set_player(name=name)
    ops.print_text(f"{name} huh? That's a weird one.\n",0.06)
    
    time.sleep(1)
    ops.print_3_dots(1)
    ops.print_text("~~I think I was...\n",0.06)
    print("1. A Warrior")
    print("2. A Wizard")
    print("3. A Rogue")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'1':
                game_state.set_player(profession='Warrior')
                break
            elif key == b'2':
                game_state.set_player(profession='Wizard')
                break
            elif key == b'3':
                game_state.set_player(profession='Rogue')
                break

    ops.print_text(f"Good, good! A {game_state.player_profession.lower()} {game_state.player_gender.lower()} named {game_state.player_name}.\n"
                   "We are piecing things together!\n"
                   "Anything else?\n",0.06)
    ops.print_3_dots(3)
    ops.print_text("Oh don't be so sad! This is stil far better than what I've expected! Now listen...\n"
                   "Normally I take people your kind to a safer place, where someone would take care of you.\n"
                   "But you seem pretty healthy!\n"
                   "...and today we have to act quick.\n"
                   #here a hardcoded location name will be replaced by one from the list
                   f"You are in {game_state.player_location}, you were dumped here by the Researchers, and you need to move on.\n"
                   "See that road over there? You're in a preatty good condition so just follow it and it will take you to my assosiates at the camp. You can't miss it. \n"
                   "Whoever greets you, tell him what happened, they will help.\n"
                   "Now go.\n\n"
                   ,0.06)
    input("Press Enter to continue.")
    menus.character_menu(game_state)