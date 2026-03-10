class Vehicle:
    def move(self):
        print("vehicle moved.")
class Car:
    def move(self):
        print("Driving on road.")
class Bicycle:
    def move(self):
        print("Pedaling on the road")
vehicle=[Car(),Bicycle()]
a=Vehicle() 
for i in vehicle:
    i.move()



