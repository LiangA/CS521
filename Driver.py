import copy
import Center
class Driver():
    def __init__(self, driverID=""):
        self.driverID = driverID
        self.center = None
        self.requests = []

    # update the request list of driver itself
    def update(self):
        if self.center != None:
            self.requests = copy.deepcopy(self.center.requests)

    # set driver id as a property, also set a getter of driver id
    @property
    def driverID(self):
        return self._driverID

    # make setter of driver id
    @driverID.setter
    def driverID(self, driverID):
        if type(driverID) == str:
            self._driverID = driverID
        else:
            raise TypeError("driver id must be a string")

    # set center as a property, also set a getter of center
    @property
    def center(self):
        return self._center
    
    # make setter of center
    @center.setter
    def center(self, center):
        if isinstance(center, Center.Center) or center == None:
            self._center = center
        else:
            raise TypeError("center must be a Center class or None")



 