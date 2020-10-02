from graph import *
from random import randint, seed, choice
#import datetime

seed(40)

amount = 100
ill = 1
healthy = amount - ill

class Person:
    size = 10

def initWorld():
    penColor('black')
    brushColor("lightgray")

    rectangle(0, 0, 500, 500)

def initPeople(amount):
    people = []
    for person in range(amount):
        people.append(person)
    
    for person in people:
        x = choice(range(0, 500 - Person.size, Person.size))
        y = choice(range(0, 500 - Person.size, Person.size))
        penColor("black")
        brushColor("white")
        rectangle(x, y, x + Person.size, y + Person.size)

if str(ill)[-1] == '1':
    ill_txt = ' больной'
else:
    ill_txt = ' больных'
ill_indicator = label(str(ill) + ill_txt, 20, 520, font=("Arial", 28))

initWorld()
initPeople(healthy)
run()

