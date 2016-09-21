"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from prac_07.car import Car


def main():
    bus = Car(180,'Bus')
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)
    print(str(bus))

    print("{}, {}".format(bus.fuel, bus.odometer))
    print("{self.fuel}, {self.odometer}".format(self=bus))

    limo = Car(100, 'Limo')
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)

    print(limo)

main()