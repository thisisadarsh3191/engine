from vector import vector
class rigidBody:
    def __init__(self,
                    centerX:float = 0.0,
                    centerY:float = 0.0, 
                    radius:float = 1.0,
                    mass:float = 1.0,
                    e:float = 1.0,
                    color:tuple = (255,255,255)
            ):
        self.mass = mass
        self.position = vector(float(centerX),float(centerY))
        self.radius = float(radius)
        self.velocity = vector()
        self.accel = vector()
        self.inverseMass = 1.0/mass if mass != 0.0 else 0.0
        self.netForce = vector()
        self.e = e
        self.color = color
        
        
    
    def addForce(self,force:vector):
        self.netForce += force

    def purgeForce(self):
        self.netForce = vector()
    
    def integrate(self,dt:float):
        if self.inverseMass == 0:
            return
        self.accel = self.netForce * self.inverseMass
        self.velocity += self.accel*dt
        self.position += self.velocity*dt

        self.purgeForce()
    
    def __repr__(self):
        return f"RigidBody:"+str({
            "position":self.position,
            "radius" :self.radius,
            "mass":self.mass,
        })
    
        