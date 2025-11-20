import os, time,shutil,colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def center_text(text):
    columns = shutil.get_terminal_size().columns
    lines = text.splitlines()
    return "\n".join(line.center(columns) for line in lines)
    
def name():
    reset()
    i = 0
    direction = 1
    max_nigg = 3
    while True:
        print(Fore.CYAN + center_text(f'{"-"*i}Made by Pataky{"-"*i}'))
        time.sleep(1)
        reset()
        i += direction
        if i >= max_nigg:
            direction = -1
        elif i <= 0:
            direction = 1
        
name()