from .simComp import SimComp
import math

class SimComp_4(SimComp):
    """
    Initializes a SimComp object, calls parent constructor
    """
    def __init__(self):
        super().__init__()

    def getNextValue(self):
        """
        Concrete method, returns the -sin^2 of the current angle value
        """
        temp = -math.sin(self.angle)**2
        self.increment()
        return temp
