from Drivers.Driver import Driver
from .sim.simComp_3 import SimComp_3

class Drvr_03(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_03')
        self.comp = SimComp_3()

    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return self.comp.getNextValue()


