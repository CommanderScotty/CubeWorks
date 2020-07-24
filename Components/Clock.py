from Components.Component import Component
from datetime import datetime


class Clock(Component):
    """
    Concrete child of the Component class.
    Represents a clock component.
    """
    def __init__(self):
        """
        Initializes a Clock object.  Calls the parent constructor.
        """
        super().__init__("clock", 1)

    def update(self, context):
        """
        Concrete method defining the abstract Component.update() method. Collects the current UTC time from the system clock in terms of milliseconds since the Unix epoch.
        """
        context[self.name] = int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000)
