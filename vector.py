
class vector:

    """A continuous, high-precision 2D Cartesian vector tracking spatial parameters ($x, y$) 
    for linear kinematics and geometric projections. This class serves as the engine's primary 
    mathematical substrate, abstracting raw component-wise coordinate operations away from the core 
    physics simulation loop."""

    def __init__(self,x:float = 0.0,y:float = 0.0):

        """Instantiates a new 2D vector primitive."""
        self.x = x
        self.y = y

    def __repr__(self)->str:
        """
        Overrides Python's native developer-facing string evaluation hook.
        Serves as an analytical tracking window
        """
        return f"Vector(x:{self.x:.3f},y:{self.y:.3f})"
    
    def __add__(self,v2:'vector') -> 'vector':
        """
        Evaluates a component-wise algebraic vector addition (self + other).
        """
        return vector(self.x+v2.x,self.y+v2.y)
    
    def __sub__(self,v2:'vector') -> 'vector':
        """
        Evaluates a component-wise algebraic vector subtraction (self - other).
        """
        return vector(self.x-v2.x,self.y-v2.y)
    

    
    def __mul__(self,scalar)->'vector':
        """
        Uniformly scales both spatial components by a real scalar number factor (vector × scalar).
        """
        return vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self,scalar:float)->'vector':
        """
        Uniformly scales both spatial components by a real scalar number factor (scalar × vector).
        """
        return vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar:float):

        """
        Dividing a vector by a scalar value: float
        """
        if scalar == 0.0:
            raise ZeroDivisionError("Cannot divide a vector by zero")
        return vector(self.x / scalar,self.y / scalar)
    

    def magSq(self) -> float:
        """
        Computes the pure algebraic dot product of the vector against itself ($x^2 + y^2$)
        """
        return (self.x ** 2 + self.y ** 2)
    

    def mag(self) -> float:
        """
        Calculates the exact geometric scalar length of the vector using the Pythagorean Theorem: sqrt{x^2 + y^2}.
        """
        return((self.x ** 2 + self.y ** 2)**0.5)
    

    def unit(self)->'vector':
        """
        Normalizes the vector, stripping away its physical scale to produce a pure directional heading vector
        """
        mag = self.mag()
        return vector(self.x / mag, self.y / mag) if mag != 0.0 else vector(1.0)
    

    def dot(self,v2:'vector')->float:
        """
        Calculates the algebraic dot product projection: self.x * other.x + self.y * other.y
        """
        return (self.x * v2.x + self.y * v2.y)