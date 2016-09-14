"""Initial attempt without string formatting"""

character = input("Enter a character: ")
print("The ASCII code for " + str(character) + " is " + str(ord(character)))
number = int(input("Enter a number between 33 and 127: "))
print("The character for " + str(number) + " is " + str((chr(number))))