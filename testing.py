import rigidBody as r
import vector

mass = r.rigidBody(400,300,10,0)
print(mass)
dt = 1/60

mass.addForce(vector.vector(10,0))
print(mass.netForce)
mass.integrate(dt)

print(mass.accel)
print(mass.inverseMass)
print(mass.position)
print(mass.velocity)
