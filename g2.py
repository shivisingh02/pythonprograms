import pgzrun 
from random import randint 
WIDTH = 1000
HEIGHT = 500 
c  = Actor('chick' , (100, 100))
w = Actor('walrus' , (500,300))
cookie = Actor('cookie' , (randint(100,700) , randint(100,300)))
speed = 5 #variable(global)
score = 0
def draw():
    screen.blit('bg' , pos = (0,0))
    c.draw()
    w.draw()
    screen.draw.text('A chicken story ' , (10,10) , color = 'red')
    screen.draw.text(f'Score: {score} ' ,(900,10) ,color = 'red')
    cookie.draw()
def update():
    global score
    if keyboard.W:
        c.y -= speed 
    elif keyboard.S:
        c.y += speed
    elif keyboard.A:
        c.x -= speed
    elif keyboard.D:
        c.x += speed 

    if c.colliderect(cookie):
        score += 1 
        cookie.pos = (randint(100,700) , randint(100,600))
pgzrun.go()
