"""
CP1404/CP5632 - Function for temperature conversion
"""

def main():

    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celcius_to_fahrenheit()
        if choice == "F":
            fahrenheit_to_celcius()

        print(MENU)

# print("Thank you.")

def celcius_to_fahrenheit():

    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))



def fahrenheit_to_celcius():

        fahrenheit = float(input("Fahrenheit: "))

        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
        #pass


main()