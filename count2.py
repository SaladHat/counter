from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
import random
import time
init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text):print(text, end='');return input()

## VARIBLES #

num = 0
add = 1
waittimeb = False
waittime = 0
randstop = False
guesses = 0
randtopnum = 15000
stopnum = -1
unum = 0

baner = f'''
{r}                          __
{r}  _________  __  ______  / /____  _____
{r} / ___/ __ \/ / / / __ \/ __/ _ \/ ___/
{r}/ /__/ /_/ / /_/ / / / / /_/  __/ /
{r}\___/\____/\__,_/_/ /_/\__/\___/_/'''

while True:
    clear()
    choice = input(f'''
{baner}
{c}--------------------------------------------
{r}[Menu]
    {y}└─[1] {m}- {g}Run
    {y}└─[2] {m}- {g}Settings
    {y}└─[3] {m}- {r}Exit
{y}====>{g}''')
    if choice == '1':
        if randstop:
            while True:
               rand = random.randint(1, int(randtopnum))
               print(rand)
               guesses += 1
            if rand == int(unum):
                   print(f"Done! Took {guesses} guesses!")
                   time.sleep(10)
                   num = 0
                   add = 1
                   waittimeb = False
                   waittime = 0
                   randstop = False
                   guesses = 0
                   randtopnum = 15000
                   stopnum = -1
                   unum = 0
                   break
        else:
            while True:
                if not int(stopnum) == int(num):
                    num += int(f'{add}')
                    print(num)
                    if waittime:
                        time.sleep(int(waittime))
                else:
                    print(f'Stopped at {stopnum}!')
                    time.sleep(10)
                    num = 0
                    add = 1
                    waittimeb = False
                    waittime = 0
                    randstop = False
                    guesses = 0
                    randtopnum = 15000
                    stopnum = -1
                    unum = 0
                    break

    elif choice == "2":
        clear()
        choice_type = input(f'''
{baner}
{c}--------------------------------------------
{b}[Select]
    {y}└─[1] {m}- {g}Pick number
    {y}└─[2] {m}- {g}Wait
    {y}└─[3] {m}- {g}Stopping number
    {y}└─[4] {m}- {g}Random number guess
    {y}└─[5] {m}- {r}Exit
{y}====>{g}''')
        if choice_type == '1':
            add = _input("Enter number: ")
        elif choice_type == '2':
            waittime = _input("Enter wait time: ")
        elif choice_type == "3":
            stopnum = _input("Enter number to stop at: ")
        elif choice_type == "4":
            randstop = True
            clear()
            choice_type2 = input(f'''
{baner}
{c}--------------------------------------------
{b}[Select]
    {y}└─[1] {m}- {g}Pick number
    {y}└─[2] {m}- {g}Pick max number (currently 1-{randtopnum})
    {y}└─[3] {m}- {r}Exit
{y}====>{g}''')
            if choice_type2 == "1":
                unum = _input(f'Enter number 1-{randtopnum}: ')
            elif choice_type2 == "2":
                randtopnum = _input("Enter max number: ")
            elif choice_type2 == "3":
                print(f'{dr}Exit...')
                exit()

        elif choice_type == '5':
            print(f'{dr}Exit...')
            exit()
    elif choice == '3':
        print(f'{dr}Exit...')
        exit()
