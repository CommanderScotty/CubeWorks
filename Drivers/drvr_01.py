from Drivers.Driver import Driver
from .sim.simComp_1 import SimComp_1

class Drvr_01(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_01')
        self.comp = SimComp_1()


    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return self.comp.getNextValue()


