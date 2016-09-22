"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from prac_08.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(Taxi)





main()