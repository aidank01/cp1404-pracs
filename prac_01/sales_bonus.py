MENU = "S - Sales Bonus \nQ (for quit)"

LOW_BONUS = 0.1
HIGH_BONUS = 0.15

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "S":
        #   ask for sales amount
        #   compare to equality test
        sales_str = input("enter sales_amount :")
        sales_float = float(sales_str)

        if sales_float < 1000:
            print("Your sales bonus is ${:.2f}".format(sales_float * LOW_BONUS))

        else:
            print("Your sales bonus is ${:.2f}".format(sales_float * HIGH_BONUS))
    else:
        print("Invalid Input")
    print(MENU)
    choice = input(">>> ").upper()
