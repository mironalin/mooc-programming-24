# Write your solution here
total = 0

total += int(input("How many times a week do you eat at the student cafeteria? "))
total *= float(input("The price of a typical student lunch? "))
total += float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {total / 7} euros")
print(f"Weekly: {total} euros")
