"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Lab7.car import Car

def main():
    bus = Car('bus', 180)
    bus.drive(30)

    limo = Car('limo', 100)
    limo.add_fuel(20)
    limo.drive(115)

    print("bus fuel =", bus.fuel)
    print("bus odo =", bus.odometer)
    print(bus)

    print("limo fuel =", limo.fuel)
    print("limo odo =", limo.odometer)
    print(limo)

main()