
from prac_07.programming_language import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    ruby.name()
    ruby.dynamic()
    ruby.reflection()
    ruby.year()
    print("mooo", ruby.name)


    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    python.name
    python.dynamic
    python.reflection
    python.year()
    print('python 2nd last print')


    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    vb.name
    vb.dynamic
    vb.reflection
    vb.year()
    print('vb last print')



    # bus = Car(180, 'Bus')
    # bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)
    # print(bus)
    #
    # print("Car {}, {}".format(bus.fuel, bus.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=bus))
    #
    # limo = Car(100, 'Limo')
    # limo.add_fuel(20)
    # print("fuel =", limo.fuel)
    # limo.drive(115)
    # print("odo =", limo.odometer)
    #
    # print(limo)

    main()
