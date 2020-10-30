import os
import sys
import msvcrt

term_size_X = os.get_terminal_size().lines
term_size_Y = os.get_terminal_size().columns


file = open(r'logo.txt')
lines = file.readlines()
file.close()

activities = [
    'Messages',
    'News',
    'Profile',
    'Exit'
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
    global selected
    if char == b'\x00':
        render(selected)
    elif char == b'P':
        if selected > 0:
            selected += 1
        else:
            pass
    elif char == b'H':
        if selected < len(activities):
            selected -= 1
        else:
            pass

def render(page):
    os.system('cls')
    if page == 0:
        messages = getMessages()
    if page == 3:
        os.system('exit')

def main():
    os.system('cls')
    drawMenu(0)
    while True:
        char = msvcrt.getch()
        if char == b'\xe0' or char == b'\r':
            char = msvcrt.getch()
        switch(char)
        drawMenu(selected)
main()
