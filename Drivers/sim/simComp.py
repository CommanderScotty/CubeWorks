import math

class SimComp:
    def __init__(self):
        """
        Initializes a SimComp object.  Sets the angle to 0
        """
        self.angle = 0

    def increment(self):
        """
        Increments the current angle by pi/12
        """
        self.angle += math.pi / 12

    def getNextValue(self):
        """
        Abstract method.  Should return the next value in a sequence defined by child class
        """
        pass
