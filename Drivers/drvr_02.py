from Drivers.Driver import Driver
from .sim.simComp_2 import SimComp_2

class Drvr_02(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_02')
        self.comp = SimComp_2()

    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return self.comp.getNextValue()


