import random
from graph import *

BASE = 500
brushColor('black')
penColor('black')

rectangle(0, 0, BASE, BASE)


brushColor('white')
penColor('white')
for x in range(BASE):
    for y in range(BASE):
        if (random.randint(0, 1)):
            cond = random.choice([0, 1, 2])
            if cond == 0:
                pass

            elif cond == 1:
                point(x, y)

            else:
                rectangle(x, y, x+2, y+2)

run()
