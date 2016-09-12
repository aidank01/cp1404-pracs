item_count = input("How many items do you have>>> ")
item_count = int(item_count)

total = 0

for i in range(0, item_count, 1):
    prompt = "Price of item " + str((i+1)) + " >>>"
    item_cost = float(input(prompt))
    total = total + item_cost

if total > 100:
    total = total * 0.9

print("Your total is $" + str(total))