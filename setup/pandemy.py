from graph import *
import random
import datetime

dt = datetime.time()
random.seed(dt.microsecond)

amount = 120
ill_amount = 2
healthy = amount - ill_amount
people = []
ill = []
illness_percent = 21

graph_pos = 0

def drawGraph(number):
    if number%20 == 0:
        penColor("black")
        brushColor("red")
        coordinates = (250 + 4*(number//20),
        580 - ill_amount//2,
        (254 + 4*(number//20)),
        580
        )
        rectangle(coordinates[0], coordinates[1], coordinates[2], coordinates[3])

class Person:
    size = 5

def initWorld():
    penColor('black')
    brushColor("lightgray")

    rectangle(0, 0, 500, 500)

def getCoordinates_x(x):
    if x > Person.size and x < 500 - Person.size:
        move_coord = random.choice([1, -1])
        return x + move_coord*Person.size
    else:
        if x <= 0:
            return 2*Person.size
        else:
            return 500 - 2*Person.size

def getCoordinates_y(y):
    if y > Person.size and y < 500 - Person.size:
        move_coord = random.choice([1, -1])
        return y + move_coord*Person.size

    else:
        if y <= 0:
            return 2*Person.size
        else:
            return 500 - 2*Person.size

def initPeople(amount):
    for person in range(amount):
        x = random.choice(range(0, 500 - Person.size, Person.size))
        y = random.choice(range(0, 500 - Person.size, Person.size))
        penColor("black")
        brushColor("white")
        obj = rectangle(x, y, x + Person.size, y + Person.size)
        people.append(obj)

def initImpostors(amount):
    for impostor in range(amount):
        x = random.choice(range(0, 500 - Person.size, Person.size))
        y = random.choice(range(0, 500 - Person.size, Person.size))
        penColor("black")
        brushColor("red")
        obj = rectangle(x, y, x + Person.size, y + Person.size)
        ill.append(obj)

def spread():
    global ill_amount
    for impostor in ill:
        ill_coord_x = xCoord(impostor)
        ill_coord_y = yCoord(impostor)
        for person in people:
            person_coord_x = xCoord(person)
            person_coord_y = yCoord(person)
            first_condition = person_coord_x == ill_coord_x or person_coord_x == ill_coord_x - Person.size or person_coord_x == ill_coord_x + Person.size
            second_condition = person_coord_y == ill_coord_y or person_coord_y == ill_coord_y - Person.size or person_coord_y == ill_coord_y + Person.size
            if first_condition and person_coord_y == ill_coord_y:
                #ill_index = random.choice(range(100-illness_percent))    
                #if ill_index == 0:
                    changeFillColor(person, "red")
                    ill.append(person)
                    people.remove(person)
                    ill_amount += 1

            elif second_condition and person_coord_x == ill_coord_x:
                #ill_index = random.choice(range(100-illness_percent))     
                #if ill_index == 0:
                    changeFillColor(person, "red")
                    ill.append(person)
                    people.remove(person)
                    ill_amount += 1


def drawLabel(ill_amount):
    if str(ill_amount)[-1] == '1' and str(ill_amount)[-2] != '1':
        ill_txt = ' больной'
    else:
        ill_txt = ' больных'
    ill_indicator = label(str(ill_amount) + ill_txt, 20, 530, font=("Arial", 28))

def movePeople():
    for obj in people:
        old_x = coords(obj)[0]
        old_y = coords(obj)[1]
        move = random.choice([1, 2])
        if move == 1:
            moveObjectTo(obj, getCoordinates_x(old_x), old_y)
        elif move == 2:
            moveObjectTo(obj, old_x, getCoordinates_y(old_y))

def moveImpostors():
    for obj in ill:
        old_x = coords(obj)[0]
        old_y = coords(obj)[1]
        move = random.choice([1, 2])
        if move == 1:
            moveObjectTo(obj, getCoordinates_x(old_x), old_y)
        elif move == 2:
            moveObjectTo(obj, old_x, getCoordinates_y(old_y))

def update():
    global graph_pos
    graph_pos += 1
    drawGraph(graph_pos)
    movePeople()
    moveImpostors()
    spread()
    drawLabel(ill_amount)

onTimer(update, 50)
initWorld()
initPeople(healthy)
initImpostors(ill_amount)
run()

