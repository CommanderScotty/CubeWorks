from Drivers.Driver import Driver
from .sim.simComp_7 import SimComp_7

class Drvr_07(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_07')
        self.comp = SimComp_7()

    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return self.comp.getNextValue()


