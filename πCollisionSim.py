from vector import vector
import pygame
import rigidBody as r
from pygame import gfxdraw as gfx
import collision as c


white=(255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (255,0,0)
green = (0,255,0)

bodyA = r.rigidBody(30,590,10,1,red)
bodyB= r.rigidBody(100,590,10,10,green)

bodyA.velocity = vector(10,0)

pygame.init()
res = (800,600)
dt = 0.01
screen = pygame.display.set_mode(res)
screen.fill(gray)
particles = [bodyA,bodyB]

gravity = vector(0,900)

def objectRun(body:r.rigidBody):
    #Adding forces
    body.addForce(gravity)
    body.integrate(dt)

    #collision
    c.wallCollisionX(body,res)
    c.wallCollisionY(body,res)


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

"game loop"
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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



