from Drivers.Driver import Driver
from .sim.simComp_5 import SimComp_5

class Drvr_05(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_05')
        self.comp = SimComp_5()

    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return self.comp.getNextValue()


