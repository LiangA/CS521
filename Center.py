import Request
import Driver
import os
class Center():
    def __init__(self, name="", region=""):
        self.name = name
        self.region = region
        self.__drivers = []
        self.__requests = []
        self.__loadRequest()

    # set requests as a property, also set a getter of __requests
    # note here, this property is set for Driver class to use
    # "__request" is not the same as "reqeusts"
    @property
    def requests(self):
        return self.__requests

    # attach driver into driver list
    def attach(self, driver):
        if isinstance(driver, Driver.Driver):
            self.__drivers.append(driver)
            driver.center = self
            return True
        else:
            print("invalid input type")
            return False

    # detach driver into driver list
    def detach(self, driver):
        if isinstance(driver, Driver.Driver):
            try:
                self.__drivers.remove(driver)
                driver.center = None
            except:
                print("the driver is not in driver list")
            return True
        else:
            print("invalid input type")
            return False

    # notify drivers to get new request list
    def notify(self):
        for d in self.__drivers:
            d.update()

    # when the center is made, load the order tickets
    def __loadRequest(self):
        self.__batch = []
        for filename in os.listdir("./requests"):
            if os.path.isfile("./requests/" + filename) and filename.endswith(".txt"):
                with open("./requests/" + filename, "r") as file:
                    self.__batch.append(file.read())
                    
    # this is the function that processes the orders(push information to drivers for 3 batches)
    def run(self): 
        for b in self.__batch:
            lines = b.split("\n")
            for line in lines:
                req = line.split(",")
                self.__requests.append(Request.Request(req[0], req[1], req[2], req[3], req[4]))
            self.notify()

    # repr function shows the information about this object
    def __repr__(self):
        return f"name:{self.name} region:{self.region} repr:{super().__repr__()}"

    # str function is a little bit informal way to present a object
    def __str__(self):
        return f"This center is {self.name} located at {self.region}"