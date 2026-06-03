import pygame
import pygame.gfxdraw as gfx

white = (255,255,255)
black = (0,0,0)

pygame.init()
clock = pygame.time.Clock()


res = (800,600)
screen = pygame.display.set_mode(res,pygame.SCALED,vsync=1)
screen.fill(white)

circleX = 400.0
circleY = 0.0
radius =20

"acceleration scaled from 9.8 m/s^2 to fit this window is about 1200 pixels/s^2"
acceleration = 1200.0
velocity = 0.0

"Game Loop"
run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    "Creating an instantaneous time element and" 
    "making sure the time element does not last more than 0.1 seconds"
    # dt = min(clock.tick(60)/1000,0.1)
    dt = 0.01666
    screen.fill(white)

    "gfx circle uses transparent points to make the circle look solid,"
    "Unlike normal pygame.draw.circle which has weird spots"
    # pygame.draw.circle(screen,black,(circleX,circleY),radius)
    gfx.aacircle(screen,int(circleX),int(circleY),radius,black)
    gfx.filled_circle(screen,int(circleX),int(circleY),radius,black)

    """Storing previous velocity to determine max height of particle after bouncing
    Done by checking if previous velocity (prevVelo) and current velocity (velocity)
    Are of opposite signs and that particle is falling downwards in the next instant
    Commented as log not required now"""
    prevVelo = velocity

    velocity = velocity + acceleration*dt
    circleY = circleY + velocity*dt

    if prevVelo*velocity < 0 and velocity > 0:
        print(circleY)
    # print("acceleration:", acceleration)

    """Finding how much depth particle has travelled so that the it 
        goes back perfectly above in the next dt
        2*penetration done because particle has to go penetration distance from
        below screen and then another equal distance as it moves up"""
    
    if circleY+radius >= 600 and velocity>0:
        penetration = circleY+radius - 600

        velocity = (velocity * -1)
        circleY = circleY - (2*penetration)


    pygame.display.flip()   

pygame.quit()