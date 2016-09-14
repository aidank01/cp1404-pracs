try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print(fraction)
print("Finished")

#1. ValueError will occur when numerator or denominator are not integers
#2. ZeroDivisionError will occur when denominator are zero
#3. Yes, denominator could be prompted to be any non-zero float.