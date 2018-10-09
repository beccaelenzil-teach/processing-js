def setup():
    size(1000, 1000)
    noStroke()

def draw():
    background(126)
    ellipse(mouseX, mouseY+16, 33, 33)   # Top circle
    ellipse(mouseX+20, mouseY+50, 33, 33)   # Middle circle
    ellipse(mouseX-20, mouseY+84, 33, 33)   # Bottom circle