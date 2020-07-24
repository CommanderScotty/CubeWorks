from .simComp import SimComp
import math

class SimComp_2(SimComp):
    """
    Initializes a SimComp object, calls parent constructor
    """
    def __init__(self):
        super().__init__()

    def getNextValue(self):
        """
        Concrete method, returns the tan of the current angle value
        """
        temp = math.tan(self.angle)
        self.increment()
        return temp
