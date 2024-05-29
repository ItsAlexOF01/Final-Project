
x=150
dirX=1
y=0
y1=0
y2=3
y3=5
y4=10
y5=13
y6=15
dirY=1
Damage=0
pont=0
randomX=100
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
  # работает правильно, даже если rectMode стоит CENTER
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False

    






def setup():
    size(900,900)
    frameRate(150)
    fill(35,255,3)
    rect(1,700,50,50)
    rect(51,700,50,50)
    rect(101,700,50,50)
    rect(151,700,50,50)
    rect(201,700,50,50)
    rect(251,700,50,50)
    rect(301,700,50,50)
    rect(351,700,50,50)
    rect(401,700,50,50)
    rect(451,700,50,50)
    rect(501,700,50,50)
    rect(551,700,50,50)
    rect(601,700,50,50)
    rect(651,700,50,50)
    rect(701,700,50,50)
    rect(751,700,50,50)
    rect(801,700,50,50)
    rect(851,700,50,50)
    rect(900,700,50,50)
    fill(62,4,4)
    rect(1,800,50,50)
    rect(51,800,50,50)
    rect(101,800,50,50)
    rect(151,800,50,50)
    rect(201,800,50,50)
    rect(251,800,50,50)
    rect(301,800,50,50)
    rect(351,800,50,50)
    rect(401,800,50,50)
    rect(451,800,50,50)
    rect(501,800,50,50)
    rect(551,800,50,50)
    rect(601,800,50,50)
    rect(651,800,50,50)
    rect(701,800,50,50)
    rect(751,800,50,50)
    rect(801,800,50,50)
    rect(851,800,50,50)
    rect(900,800,50,50)
    fill(62,4,4)
    rect(1,750,50,50)
    rect(51,750,50,50)
    rect(101,750,50,50)
    rect(151,750,50,50)
    rect(201,750,50,50)
    rect(251,750,50,50)
    rect(301,750,50,50)
    rect(351,750,50,50)
    rect(401,750,50,50)
    rect(451,750,50,50)
    rect(501,750,50,50)
    rect(551,750,50,50)
    rect(601,750,50,50)
    rect(651,750,50,50)
    rect(701,750,50,50)
    rect(751,750,50,50)
    rect(801,750,50,50)
    rect(851,750,50,50)
    rect(900,750,50,50)
    fill(62,4,4)
    rect(1,850,50,50)
    rect(51,850,50,50)
    rect(101,850,50,50)
    rect(151,850,50,50)
    rect(201,850,50,50)
    rect(251,850,50,50)
    rect(301,850,50,50)
    rect(351,850,50,50)
    rect(401,850,50,50)
    rect(451,850,50,50)
    rect(501,850,50,50)
    rect(551,850,50,50)
    rect(601,850,50,50)
    rect(651,850,50,50)
    rect(701,850,50,50)
    rect(751,850,50,50)
    rect(801,850,50,50)
    rect(851,850,50,50)
    rect(900,850,50,50)
    fill(246,255,5)
    rect(700,120,150,150)


def draw():
    global randomX
    global pont
    background(3,255,219)
    rectMode(CENTER)
    if collideRectRect(randomX,780, 50, 50, x,780,50,50):
        randomX=random(100,800)
        fill(255,0,0)
        pont+=1
    else:
        fill(255)
    rect(randomX,780, 50, 50)
    global x, y
    global dirX, dirY
    text(pont,50,100)
    fill(0,0,0)
    rect(x,780,100,100)
    textSize(100)
    text(pont,50,100)
    if key == 'd' or key == 'D':
        x=x+dirX
    if key == 'a' or key == 'A':
        x=x-dirX
        



    
