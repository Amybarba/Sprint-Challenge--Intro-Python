# Write classes for the following class hierarchy:
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
# base class is Vehicle
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v

# base


class Vehicle:
    pass


class FlightVehicle(Vehicle):
    pass


class Starship(FlightVehicle):
    pass

# base
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v


# base
class GroundVehicle(Vehicle):
    pass


class Airplane(FlightVehicle):
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# [Car]  [Motorcycle]
#

#
# e.g.
#
# class Whatever:
#    pass
#
# Put a comment noting which class is the base class
