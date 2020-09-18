from graph import *
from PIL import Image

image = Image.open('yarik.jpg')
WIDTH = image.size[0]
HEIGHT = image.size[1]
pix = image.load()

SIZE = 8

def drawOneRect(x, y, rotated):
    global SIZE

    if rotated:
        polygon([
                (x, y),
                (x, y + SIZE),
                (x + SIZE, y),
                (x + SIZE, y + SIZE)
            ])
    else:
        polygon([
                (x, y),
                (x + SIZE, y),
                (x, y + SIZE),
                (x + SIZE, y + SIZE)
            ])

def draw(level, amount):
    rotated = False
    for j in range(level):
        for i in range(amount):
            red = pix[j, i][0]
            #TODO: ADD OTHER PIX
            drawOneRect(SIZE * i, SIZE * j, rotated)
            rotated = not rotated
        rotated = not rotated

draw(WIDTH, HEIGHT)
run()
