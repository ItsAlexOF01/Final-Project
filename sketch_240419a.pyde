x=0
dirX=1
y=0
dirY=1




def setup():
    size(900,900)
    background(3,255,219)
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
    global x
    global dirX
    print(mouseX, mouseY)
    fill(93,4,4)
    rect(751,600,50,100)
    if keyPressed:
        if key == 'a' or key == 'A':
            global x
            global dirX
            global y
            global dirY
            rect(x,600,50,100)
            x = x+dirX
            if x > 1:
                dirX=1
            translate(x,y)
            rotate(radians(25))
            

        
        
                
     
    
    

    
    
            

            
            

        
            


    
    
