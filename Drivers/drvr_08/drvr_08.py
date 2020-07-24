from Drivers.Driver import Driver
from .simComp_08 import getNextValue

class Drvr_08(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_08')


    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return getNextValue()


