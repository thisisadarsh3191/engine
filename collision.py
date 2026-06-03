
import rigidBody as r

def wallCollisionY(body:r.rigidBody,res:tuple):
    penYdown = body.position.y + body.radius - res[1]
    penYup = body.radius - body.position.y
    # if pen >= 0 and body.velocity.y > 0:
    #     body.velocity.y *= -e
    #     body.position.y -= 2*pen
    if penYdown >= 0 and body.velocity.y > 0:
        body.velocity.y *= -body.e
        body.position.y -= 2*penYdown
        return
    elif penYup >= 0 and body.velocity.y <0:
        print(body.velocity)
        body.velocity.y *= -body.e
        body.position.y += 2.0*penYup

def wallCollisionX(body:r.rigidBody,res:tuple):
    penXleft = body.position.x - body.radius
    penXright = body.position.x+ body.radius - res[0]
    # if pen >= 0 and body.velocity.y > 0:
    #     body.velocity.y *= -e
    #     body.position.y -= 2*pen
    if penXleft <= 0 and body.velocity.x < 0:
        body.velocity.x *= -body.e
        body.position.x -= 2*penXleft
        return
    elif penXright >= 0 and body.velocity.x >0:
        # print(body.velocity)
        body.velocity.x *= -body.e
        body.position.x -= 2.0*penXright