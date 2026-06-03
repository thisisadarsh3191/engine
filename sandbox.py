import pygame
import rigidBody as r
from vector import vector
from pygame import gfxdraw as gfx
import collision as c

white=(255,255,255)
black = (0,0,0)
gray = (128,128,128)

res = (800,600)
pygame.init()
# clock = pygame.time.clock()
dt = 0.01666


screen = pygame.display.set_mode(res)
screen.fill(gray)

def create(body:r.rigidBody):
    gfx.aacircle(
        screen,
        int(body.position.x),
        int(body.position.y),
        int(body.radius),black
    )
    gfx.filled_circle(
        screen,
        int(body.position.x),
        int(body.position.y),
        int(body.radius),black
    )

    # if circleY+radius >= 600 and velocity>0:
    #     penetration = circleY+radius - 600

    #     velocity = (velocity * -1)
    #     circleY = circleY - (2*penetration)



ball = r.rigidBody(300,400,10,10,0.9)
ball.velocity = vector(10)
gravity = vector(0,200)

"Game loop"
run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
    
    #Adding forces
    ball.addForce(gravity)
    ball.integrate(dt)

    #collision
    c.wallCollisionX(ball,res)
    c.wallCollisionY(ball,res)

    #visual rendering
    screen.fill(gray)
    create(ball)
    pygame.display.flip()

pygame.quit()