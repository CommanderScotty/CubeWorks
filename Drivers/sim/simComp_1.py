from .simComp import SimComp
import math

class SimComp_1(SimComp):
    """
    Initializes a SimComp object, calls parent constructor
    """
    def __init__(self):
        super().__init__()

    def getNextValue(self):
        """
        Concrete method, returns the cos of the current angle value
        """
        temp = math.cos(self.angle)
        self.increment()
        return temp
