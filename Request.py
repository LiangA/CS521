class Request():
    def __init__(self, id="", description="", origin="", destination="", requestTime=""):
        self.__requestID = id
        self.description = description
        self.__origin = origin
        self.__destination = destination
        self.__requestTime = requestTime

    # set destination as a property, also set a getter of destination
    @property
    def destination(self):
        return self._description

    # make setter of destination
    @destination.setter
    def destination(self, description):
        self._description = description