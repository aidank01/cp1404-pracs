"""Recoding into a loop with initial condition set to false. Once condition is true (though entering the appropriate inputs), program will end"""

exit_condition = False

while exit_condition != True:
    try:

        character = input("Enter a character: ")
        if character < 'A' or character > 'z':
            print("Error: please enter a capital or lowercase character between A and Z")
        else:
            print("The ASCII code for " + str(character) + " is " + str(ord(character)))

        number = int(input("Enter a number between 33 and 127: "))
        if number < 33 or number > 127:
            print("Error: Please enter a number from 33 to 127")
            print("The character for " + str(number) + " is " + str((chr(number))))
    except ValueError:
        print("Error: Please enter a number from 33 to 127")

"""fix errors with not remaining on first question until completed"""