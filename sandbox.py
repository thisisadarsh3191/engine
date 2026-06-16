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


ballA = r.rigidBody(300,300,10,10)
ballB = r.rigidBody(400,300,10,1000,color=red)

#give velocities here#############################


##################################################
particles = [ballA,ballB]


res = (1200,600)
pygame.init()
# clock = pygame.time.clock()
dt = 0.01


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



def objectRun(body:r.rigidBody,e:float = 1.0):
    #Adding forces
    body.addForce(body.gForce)
    body.integrate(dt)

    #collision
    c.wallCollisionX(body,res,e)
    c.wallCollisionY(body,res,e)
    
    
e = 0.8

"Game loop"
run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    for p in particles:
        objectRun(p,e)

    for i in range(0,len(particles)):
        for j in range(i+1,len(particles)):
            c.particleResolution(particles[i],particles[j])
            c.particleCollision(particles[i],particles[j],e)
    
    
    #visual rendering
    screen.fill(gray)
    for p in particles:
        create(p)
    

    pygame.display.flip()

pygame.quit()