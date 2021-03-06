from Drivers.Driver import Driver
from .sim.simComp_4 import SimComp_4

class Drvr_04(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_04')
        self.comp = SimComp_4()

    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return self.comp.getNextValue()


