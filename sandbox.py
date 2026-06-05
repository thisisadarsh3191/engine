import pygame
import rigidBody as r
from vector import vector
from pygame import gfxdraw as gfx
import collision as c

white=(255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (255,0,0)
green = (0,255,0)

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
        int(body.radius),body.color
    )
    gfx.filled_circle(
        screen,
        int(body.position.x),
        int(body.position.y),
        int(body.radius),body.color
    )

    # if circleY+radius >= 600 and velocity>0:
    #     penetration = circleY+radius - 600

    #     velocity = (velocity * -1)
    #     circleY = circleY - (2*penetration)



ballA = r.rigidBody(300,300,10,10)
ballA.velocity = vector(10)

ballB = r.rigidBody(400,300,10,20,color=red)
ballB.velocity = vector(-15)

ballC = r.rigidBody(500,300,25,100,color=green)

# gravity = vector(0,200)
particles = [ballA,ballB,ballC]

def objectRun(body:r.rigidBody):
    #Adding forces
    # body.addForce(gravity)
    body.integrate(dt)

    #collision
    c.wallCollisionX(body,res)
    c.wallCollisionY(body,res)
    


"Game loop"
run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    for p in particles:
        objectRun(p)

    for i in range(0,len(particles)):
        for j in range(i+1,len(particles)):
            c.particleResolution(particles[i],particles[j])
            c.particleCollision(particles[i],particles[j])
    
    
    #visual rendering
    screen.fill(gray)
    for p in particles:
        create(p)
    

    pygame.display.flip()

pygame.quit()