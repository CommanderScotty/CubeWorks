from .simComp import SimComp
import math

class SimComp_0(SimComp):
    """
    Initializes a SimComp object, calls parent constructor
    """
    def __init__(self):
        super().__init__()

    def getNextValue(self):
        """
        Concrete method, returns the sin of the current angle value
        """
        temp = math.sin(self.angle)
        self.increment()
        return temp
