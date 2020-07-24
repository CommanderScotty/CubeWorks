from Drivers.Driver import Driver
from .sim.simComp_6 import SimComp_6

class Drvr_06(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_06')
        self.comp = SimComp_6()

    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return self.comp.getNextValue()


