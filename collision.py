
import rigidBody as r

def wallCollisionY(body:r.rigidBody,res:tuple,e:float = 1.0):
    """Ensures particle stays within given coordinates of y"""
    penYdown = body.position.y + body.radius - res[1]
    penYup = body.radius - body.position.y
    # if pen >= 0 and body.velocity.y > 0:
    #     body.velocity.y *= -e
    #     body.position.y -= 2*pen
    if penYdown >= 0 and body.velocity.y > 0:
        body.velocity.y *= -e
        body.position.y -= penYdown
        return
    elif penYup >= 0 and body.velocity.y <0:
        print(body.velocity)
        body.velocity.y *= -e
        body.position.y += penYup

def wallCollisionX(body:r.rigidBody,res:tuple,e:float = 1.0):
    """Ensures particle stays within given coordinates of x"""
    penXleft = body.position.x - body.radius
    penXright = body.position.x+ body.radius - res[0]
    # if pen >= 0 and body.velocity.y > 0:
    #     body.velocity.y *= -e
    #     body.position.y -= 2*pen
    if penXleft <= 0 and body.velocity.x < 0:
        body.velocity.x *= -e
        body.position.x -= penXleft
        return
    elif penXright >= 0 and body.velocity.x >0:
        # print(body.velocity)
        body.velocity.x *= -e
        body.position.x -= penXright


def particleResolution(bodyA:r.rigidBody,bodyB:r.rigidBody):
    """To resolve any discrepancies in the movement of particles, avoiding any overlap"""
    radii = bodyA.radius + bodyB.radius #distance between centres when they are touching
    d = bodyA.position - bodyB.position

    if d.magSq()>radii**2:
        return 
    pen = radii - d.mag()
    normal = d.unit()
    sepOffset = normal * pen

    # bodyA.position += sepOffset
    # bodyB.position -= sepOffset
    totalInverseMass = bodyA.inverseMass+bodyB.inverseMass
    if totalInverseMass == 0.0:
        return
    bodyA.position += sepOffset*(bodyA.inverseMass/totalInverseMass)
    bodyB.position -= sepOffset*(bodyB.inverseMass/totalInverseMass)
    # print(f"Particles collided:A {bodyA.velocity}\nB{bodyB.velocity}")#debug


# "now bodies are colliding in the right way-right next to each other and not overlapping"

# def particleCollision(bodyA:r.rigidBody,bodyB:r.rigidBody,e:float=1.0):
#     v_rel = bodyA.velocity - bodyB.velocity
#     normal = (bodyA.position - bodyB.position).unit()
#     vNormal = v_rel.dot(normal)
#     if vNormal >= 0:
#         return
#     mA,mB = bodyA.mass,bodyB.mass
#     vA_normal = bodyA.velocity.dot(normal)
#     vB_normal = bodyB.velocity.dot(normal)
#     finalVelocityA = ((mA-e*mB) * vA_normal + ((1+e)*mB) * vB_normal) / (mA+mB)
#     finalVelocityB = (mA * (1+e) * vA_normal + vB_normal * (mB - mA*e)) / (mA+mB)
#     # bodyA.velocity = finalVelocityA
#     # bodyB.velocity = finalVelocityB
#     deltaV_a = (finalVelocityA - vA_normal)*normal
#     deltaV_b = (finalVelocityB - vB_normal)*(-1*normal)
#     bodyA.velocity += deltaV_a
#     bodyB.velocity += deltaV_b

def particleCollision(bodyA:r.rigidBody,bodyB:r.rigidBody,e:float = 1.0):
    rSum = bodyA.radius + bodyB.radius
    sep = bodyA.position - bodyB.position

    if sep.magSq()>rSum**2:
        return
    
    normal = sep.unit()
    uRel = bodyA.velocity - bodyB.velocity
    vN = uRel.dot(normal)
    if vN >= 0:
        return
    impulse = (-1*(1+e)*vN)/(bodyA.inverseMass+bodyB.inverseMass)

    bodyA.velocity += (impulse*bodyA.inverseMass)*normal
    bodyB.velocity -= (impulse*bodyB.inverseMass)*normal
    print("Collision has occured")
    print(f"Body A: {bodyA.velocity}\nBody B:{bodyB.velocity}")

