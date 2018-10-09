import random

circle_list = []


def setup():
    size(1000,1000)
    background(255)
    for i in range(100):
        circ = circle(random.randint(1,1000), random.randint(1,1000), random.randint(9,11))
        circle_list.append(circ)
    
    
def draw():
    for circ in circle_list:
        circ.change_x = circ.change_x*-1
        circ.change_y = circ.change_y*-1
        circ.x += circ.change_x
        circ.y += circ.change_y
        ellipse(circ.x,circ.y,circ.d,circ.d)
        fill(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
    d2 = random.randint(19,21)
    ellipse(mouseX,mouseY,d2,d2)
    

class circle():
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.change_x = 1
        self.change_y = 1
        self.d = d 