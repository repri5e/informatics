
from graph import *
import random
brushColor('green')
penColor(0, 0, 0)
c=(random.randint(0, 400))
b=(random.randint(0, 400))
obj=rectangle(c, b, c+10, b+10)

def moveSnake(xNew, yNew):
  global x, y, c, b, n, obj, snake
  if ([c,b, c+10, b+10]==coords(snake[0])):
    c=(random.randint(0, 400))
    b=(random.randint(0, 400))
    moveObjectTo(obj, c, b)
    
  for k in range(len(snake)-1,0,-1):
    newCoord = coords(snake[k-1])
    moveObjectTo(snake[k], newCoord[0], newCoord[1])
  moveObjectTo(snake[0], xNew, yNew)
  x = xNew
  y = yNew
  for k in range(len(snake)-1,0,-1):
    if xCoord(snake[0])==xCoord(snake[k]) and  yCoord(snake[0])==yCoord(snake[k]):
       close()
    

def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT: 
    dx = -1; dy = 0 
  elif event.keycode == VK_RIGHT:
    dx = 1; dy = 0 
  elif event.keycode == VK_UP:
    dx = 0; dy = -1 
  elif event.keycode == VK_DOWN:
    dx = 0; dy = 1 
  elif event.keycode == VK_SPACE:
    dx = dy = 0
  elif event.keycode == VK_ESCAPE:
    close() 

def doMove():
  global dx, dy
  if dx or dy:
    xNew = x + dx*a
    yNew = y + dy*a
    if xNew < 0: 
      dx = 0 
      if yNew > 0: dy = -1
      else: dy = 1
    elif yNew < 0:
      dy = 0
      if xNew > 0: dx = -1
      else: dx = 1
    elif xNew > 400-a:
      dx = 0
      if yNew < 400-a: dy = 1
      else: dy = -1
    elif yNew > 400-a:  
      dy = 0
      if xNew < 400-a: dx = 1
      else: dx = -1
    else: moveSnake(xNew, yNew)
 
brushColor("blue")
rectangle(0, 0, 400, 400)

x = 100; y = 100
dx = 0;  dy = 0
a = 10; N = 20

snake = []
penColor("yellow")
brushColor("yellow")
for i in range(0,N):
  snake.append( rectangle(x+i*a, y, x+i*a+a, y+a) )
  brushColor("green")

onKey(keyPressed)
onTimer(doMove, 50)

run()