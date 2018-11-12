

def setup():
    size(640,480)
    
    
def draw():

    noStroke()
    background(255,255,100)
    fill(0,0,100)
    
    for i in range(0, 650, 60):
        rect(i, height/2, 50,50)
        
