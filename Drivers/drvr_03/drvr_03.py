from Drivers.Driver import Driver
from .simComp_03 import getNextValue

class Drvr_03(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_03')


    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return getNextValue()


