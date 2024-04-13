x=0
dirX=0
y=0
dirY=0



def setup():
    size(900,900)
    
    
def draw():
    if keyPressed:
        if key == 'q' or key == 'Q':
            background(92,255,0)
        if key == 'w' or key == 'W':
            background(0,255,206)
        if key == 'e' or key == 'E':
            background(255,0,0)
        if key == 'r' or key == 'R':
            background(255,234,0)
        if key == 't' or key == 'T':
            background(250,0,255)
        if key == 'y' or key == 'Y':
            background(0,44,255)
    
    mouseClicked():
        if mousePressed == True:
            
