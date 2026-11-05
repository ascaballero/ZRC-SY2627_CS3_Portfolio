1. ​a. Duck typing means Python treats an object based on what it can do (its methods and attributes) rather than what class it inherits from. If it walks and quacks like a duck, it's a duck!

    ​b. The Car needed the exact same methods and attributes that the loop called (like a speak() method and an alive attribute).


2. 
class Vehicle:
    def move(self):
        pass

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)


3. This code uses polymorphism because the start_trip() function doesn't care what kind of object it gets. As long as the object has a .move() method, it works for any of them.