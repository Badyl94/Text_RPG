import time
import sys

def type_out(tekst, delay=0.1):
    """
    Wypisuje tekst literka po literce z opóźnieniem.
    
    :param tekst: Tekst do wypisania
    :param delay: Opóźnienie między literami (sekundy), domyślnie 0.1
    """
    for litera in tekst:
        print(litera, end='', flush=True)
        time.sleep(delay)
    print()  # nowa linia na końcu

#type_out("Welcome to the Text RPG!", 0.05)