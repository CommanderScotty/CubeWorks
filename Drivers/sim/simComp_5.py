from .simComp import SimComp
import math

class SimComp_5(SimComp):
    """
    Initializes a SimComp object, calls parent constructor
    """
    def __init__(self):
        super().__init__()

    def getNextValue(self):
        """
        Concrete method, returns the cos^2 of the current angle value
        """
        temp = math.cos(self.angle)**2
        self.increment()
        return temp
