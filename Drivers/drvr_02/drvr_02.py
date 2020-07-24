from Drivers.Driver import Driver
from .simComp_02 import getNextValue

class Drvr_02(Driver):
    def __init__(self):
        """
        Initializes a dummy driver that is used to test the framework.
        """
        super().__init__('drvr_02')


    def read(self):
        """
        A dummy driver component that "reads data" from a simulated hardward component.
        """
        return getNextValue()


