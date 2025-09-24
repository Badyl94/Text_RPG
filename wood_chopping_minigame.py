import random
import math
import time
import os
import sys
import msvcrt


def chopping_style_check():
    default_time = 45
    print("Press Enter to choose your chopping style")
    for value in loop_1_to_100(1):
        sys.stdout.write(f'You accumulate your strengh: {value}\033[K\n')
        #sys.stdout.write("\n")
        sys.stdout.flush()
        sys.stdout.write("\033[F")
    print('\n\n---------------------------------')    
    if value <= 70:
        print("You chose weak but precise strikes!")
        aim_mod = 5
    elif 70 < value <= 90:
        print("You chose balanced strikes!")
        aim_mod = 3
    else:
        print("You chose strong but wild strikes!")
        aim_mod = 1
    print('---------------------------------\n')  
    chopping(default_time, aim_mod)
#tu zrobic if value to wtedy speed mode
#return odpowiedniej wartosci i niech tego returna od razu uzywa funkcja w mainie

def chopping(time_limit, aim_mod):
    round_won = 0
    remaining_time = time_limit

    try:
        while round_won < 6:
            exact_spot = random.randint(1, 100)
            print(f'Round {round_won + 1} - You have {math.floor(remaining_time)} seconds to chop down the trees!')
            
            if round_won != 0:
                print("\nWhat do you want to do?")
                print("1. Start next round")
                print("2. Collect wood and leave\n")
                #input() ?
                while True:
                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b'1':
                            print("You chose to start the next round!\n")
                            break
                        elif key == b'2':
                            print("You chose to collect your wood and leave!\n")
                            give_wood(aim_mod, round_won)
                            return 
                        else:
                            print(f"Invalid key. Press 1 or 2.")
                    time.sleep(0.05)
        

            print("\nPress Enter when you are ready to start chopping")
            #albo input()
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b'\r':
                       break
                    
            start_time = time.time()
            wood_health = 4
            while wood_health > 0:
                for aim_spot in loop_1_to_100(aim_mod):
                    time_left = remaining_time - (time.time() - start_time)
                    if time_left <= 0:
                        raise TimeOut

                    sys.stdout.write(f"\rCurrent aim at position: {aim_spot:3d} || Time left: {int(time_left)} seconds")
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                    sys.stdout.write("\033[F")

                os.system('cls')
                print(f'You aimed at: {aim_spot} \n')

                if exact_spot - 5 < aim_spot < exact_spot + 5:
                    print("Great hit! You hit the exact spot!\n")
                    wood_health -= 4
                elif exact_spot - 15 < aim_spot < exact_spot + 15:
                    print("Good hit! You were close!\n")
                    wood_health -= 2
                elif exact_spot - 25 < aim_spot < exact_spot + 25:
                    print("You hit the tree but were far from the spot!\n")
                    wood_health -= 1
                else:
                    print(f'Not even close! Critical spot is on {exact_spot}!')

                print(f'Wood health: [{wood_health}/4]\n')

            print("\nYou chopped down the tree!!!!!\n")
            round_won += 1

            elapsed = time.time() - start_time
            remaining_time -= elapsed

            if remaining_time <= 0:
                raise TimeOut

        print(f"Remaining time: {int(remaining_time)} seconds")
        if round_won < 6:
            input("Press Enter to continue to the next round.")
        else:
            print("You chopped all the trees!")
            give_wood(aim_mod, round_won)
            return

    except TimeOut:
        print("\nYou ran out of time and you faint!\n")
        return

    

def time_check(start_time, time_limit):
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        raise TimeOut
    return time_limit - int(elapsed_time)


class TimeOut(Exception):
    pass

def loop_1_to_100(speed):
    current_value = 0
    direction = 1
    
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                return current_value

        yield current_value

        current_value += direction    
        if current_value == 100:
            direction = -1
        elif current_value == 0:
            direction = 1  

        time.sleep(0.015 * speed)

def give_wood(aim_mod, achieved_level):
    chopping_rewards = {
        3: {1: 50, 2: 100, 3: 150, 4: 400, 5: 500, 6: 600},
        2: {1: 60, 2: 125, 3: 185, 4: 500, 5: 625, 6: 750},
        1: {1: 85, 2: 175, 3: 260, 4: 700, 5: 875, 6: 1050}
    }
    print(f'You collected {chopping_rewards[aim_mod][achieved_level]} wood')
    #return chopping_rewards[aim_mod][achieved_level]
    time.sleep(2)
    exit() 