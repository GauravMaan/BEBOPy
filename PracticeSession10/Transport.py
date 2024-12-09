class Transport:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move method")

class Airplane(Transport):
    def move(self):
        print("The airplane is flying in the sky.")

class Ship(Transport):
    def move(self):
        print("The ship is sailing on the water.")

class Car(Transport):
    def move(self):
        print("The car is driving on the road.")
transports = [
    Airplane(),
    Ship(),
    Car(),
    Airplane(),
    Ship()
]
for transport in transports:
    transport.move()