from graphics import *
from time import *
from random import *
from math import *

GWin = GraphWin('Game Window', 600,600)
GWin.setBackground('Light Sky Blue')
Ground = Rectangle(Point(-1,450),Point(600,600))
Ground.setFill('Light Green')
Ground.draw(GWin)

 
def create(targets):
    clay = Circle(Point(300,300),8).draw(GWin)
    targets.append(clay)
    return targets
    
def move(targets,run):
    while run == 1:
        for target in targets:
                target.move(10,0)
        sleep(0.5)
        if len(targets) == 5:
            run = 0
        else:
            move(create(targets),run)
            
    while run == 0:
        for target in targets:
            target.move(10,0)
        sleep(0.5)
        
        
targets = []
targets = create(targets)
run = 1
move(targets,run)

