import os
import sys

term_size_X = os.get_terminal_size().lines
term_size_Y = os.get_terminal_size().columns


file = open(r'logo.txt')
lines = file.readlines()
file.close()

activities = [
    'Messages',
    'News',
    'Profile'
]
selected = 0

def drawMenu(chosen):
    os.system('cls')
    for line in lines:
        print(line, end='')
    print('\n')
    print('Welcome to Stove!')
    print('\n')
    for i in range(len(activities)):
        if i == chosen:
            print('* ', end='')
        else:
            print('  ', end='')
        print(activities[i])

def getMessages():
    pass
#TODO: add message loading from database file

def switch(char):
    if char == 0x24:
        render(selected)
    elif char == 0x26:
        if selected > 0:
            selected -= 1
        else:
            pass
    elif char == 0x28:
        if selected < len(activities):
            selected += 1
        else:
            pass

def render(page):
    os.system('cls')
    if page == 0:
        messages = getMessages()

def main():
    os.system('cls')
    drawMenu(0)
    while True:
        char = sys.stdin.read(1)
        print(char)
        switch(char)
        drawMenu(selected)
main()
