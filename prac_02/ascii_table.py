"""Recoding into a loop with initial condition set to false. Once condition is true (though entering the appropriate inputs), program will end"""

def get_number():

    exit_condition = False

    while exit_condition != True:
        try:

            # character = input("Enter a character: ")
            # if character < 'A' or character > 'z':
            #     print("Error: please enter a capital or lowercase character between A and Z")
            # else:
            #     print("The ASCII code for " + str(character) + " is " + str(ord(character)))

            number = int(input("Enter a number (10-50): "))
            if number < 10 or number > 50:
                print("Error: Please enter a valid number!")
            else:
                print("The character for " + str(number) + " is " + str((chr(number))))
        except ValueError:
            print("Error: Please enter a valid number!")

get_number()


