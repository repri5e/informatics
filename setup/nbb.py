from graph import *

AMOUNT = int(input())

SIZE = 1
BLUE = 0
penSize(SIZE)


HIGHER = 500
LOWER = 250
STEP_HIGHER = HIGHER / (AMOUNT-1)
STEP_LOWER = LOWER / (AMOUNT-1)

def drawLine(number):
    global STEP_HIGHER, STEP_LOWER, LOWER, HIGHER
    line(STEP_HIGHER*number, 0, (HIGHER-LOWER)/2 + STEP_LOWER*number, 400)

for i in range(AMOUNT):
    if i < AMOUNT / 2:
        BLUE += 15
        SIZE += 0.5
        penSize(SIZE)
        penColor(BLUE//2, 0, BLUE)
    else:
        BLUE -= 15
        SIZE -= 0.5
        penSize(SIZE)
        penColor(BLUE//2, 0, BLUE)
    drawLine(i)

run()
