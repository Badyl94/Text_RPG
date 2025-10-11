import time

def print_text(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def erase_text_len(text_len, delay=0.03):
    for i in range(text_len):
        print('\b \b', end='',flush=True)
        time.sleep(delay)
        i+=1

def print_3_dots(times):
    for x in range(times):
        for x in range(3):
            print('.', end='', flush=True)
            time.sleep(0.3)
        for x in range(3):
            print('\b \b', end='', flush=True)
            time.sleep(0.15)


