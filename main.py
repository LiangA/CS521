import Driver
import Center
print("------test 1------")
test1 = Center.Center("Test1", "A")
# test the __repr__ and __str__
print(test1.__repr__())
print(test1)
# the initial state of request list is an empty list
assert test1.requests == [], "requests is not empty"
# after run(), the request list would be the data in 3 batches
test1.run()
assert test1.requests != [], "request should have data"
# let's see what is inside the reqeust list
for i in test1.requests:
    print(i, end=", ")
print()
print("------end of test 1------")
print()
print("------test 2------")
# by the test1, we make sure that the requests are read from the files correctly
# next, we will test if multiple drivers can attatch to the center and get informed

test2 = Center.Center("Test2", "B")
a = Driver.Driver("a")
b = Driver.Driver("b")
c = Driver.Driver("c")
test2.attach(a)
test2.attach(b)
test2.attach(c)
# I didn't implement getter of driver list because it is not nessary
# If we can be sure that all the drivers attached get the right information, what driver list is doesn't matter
# so first we call run() to run the informing flow
test2.run()
# after run(), the reference of requests in Driver should be the same as the Center
print("testing driver a...")
assert id(a.requests) == id(test2.requests), "driver is not updated"
print("pass")
print("testing driver b...")
assert id(b.requests) == id(test2.requests), "driver is not updated"
print("pass")
print("testing driver c...")
assert id(c.requests) == id(test2.requests), "driver is not updated"
print("pass")
# note that both Driver.requests and Center.requests are getter without setter
print("attach success")
print("------end of test 2------")
print()
print("------test 3------")
# let's try detach
test3 = Center.Center("Test3", "C")
test3.attach(a)
test3.attach(b)
test3.attach(c)
# Center test3 attaches a, b and c, now lets detach c
test3.detach(c)
# run the flow
test3.run()
# now, the request list of a and b should differ from c(c.center should be None)
print("testing driver a...")
assert id(a.requests) == id(test3.requests), "driver is not updated"
print("pass")
print("testing driver b...")
assert id(b.requests) == id(test3.requests), "driver is not updated"
print("pass")
print("testing driver c...")
assert id(c.requests) != id(test3.requests), "driver should not be updated"
assert c.center == None, "detached from center, center should be None"
print("pass")
print("detach success")
print("------end of test 3------")

# all test are passed! the program runs well



