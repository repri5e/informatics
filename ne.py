from graph import *

AMOUNT = int(input())
SIDE = 200
STEP = SIDE / (AMOUNT - 1)

def drawLine(number):
    global STEP
    line(0, STEP*number, SIDE, SIDE - STEP*(number))

for i in range(AMOUNT):
    drawLine(i)

run()
