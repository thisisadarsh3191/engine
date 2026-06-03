import math

class vector:
    def __init__(self,x:float = 0.0,y:float = 0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector(x:{self.x:.3f},y:{self.y:.3f})"
    
    def __add__(self,v2:'vector') -> 'vector':
        return vector(self.x+v2.x,self.y+v2.y)
    def __sub__(self,v2:'vector') -> 'vector':
        return vector(self.x+v2.x,self.y+v2.y)
    def dot(self,v2:'vector')->'vector':
        return vector(self.x * v2.x + self.y * v2.y)
    def __mul__(self,scalar)->'vector':
        return vector(self.x * scalar, self.y * scalar)
        
    def magSq(self):
        return (self.x ** 2 + self.y ** 2)
    def len(self):
        return((self.x ** 2 + self.y ** 2)**0.5)
    def unit(self):
        mag = len(self)
        return vector(self.x / mag, self.y / mag)
    