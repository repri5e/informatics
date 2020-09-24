from graph import *

radius = 10
start_point_X = radius/2 
start_point_Y = 0
acceleration_Y = 10
acceleration_X = 1
velocty_X = 20
velocity_Y = 0

started = False

brushColor("blue")
rectangle(0, 0, 500, 600)

brushColor("yellow")
penColor("yellow")
arrow = polygon([
        (start_point_X, start_point_Y),
        (start_point_X + 20, start_point_Y + radius),
        (start_point_X, start_point_Y + 2*radius),
        ])

ball = circle(start_point_X, start_point_Y, radius)

def keyPressed(event):
    global started
    global start_point_Y
    global start_point_X
    if not started:
        if event.keycode == VK_DOWN:
            if start_point_Y < 500 - radius:
                start_point_Y += 2*radius
                choose(start_point_Y)

        if event.keycode == VK_UP:
            if start_point_Y > radius:
                start_point_Y -= 2*radius
                choose(start_point_Y)

        if event.keycode == VK_RETURN:
            started = True
            deleteObject(arrow)
    else:
        if event.keycode == VK_ESCAPE
def choose(start_point_Y):
    penColor("yellow")
    brushColor("yellow")
    moveObjectTo(arrow, start_point_X, start_point_Y)

def moveBall(directX, directY):
    new_X = getCoordinates()
    #TODO: add others

onKey(keyPressed)
run()