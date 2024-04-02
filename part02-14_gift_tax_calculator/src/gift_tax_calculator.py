# Write your solution here
gift = int(input("Value of gift: "))
tax = 0

if gift > 1_000_000:
    tax = 142_100 + (gift - 1_000_000) * 0.17
elif gift > 200_000:
    tax = 22_100 + (gift - 200_000) * 0.15
elif gift > 55_000:
    tax = 4700 + (gift - 55_000) * 0.12
elif gift > 25_000:
    tax = 1700 + (gift - 25_000) * 0.10
elif gift > 5000:
    tax = 100 + (gift - 5000) * 0.08
else:
    print("No tax!")

if tax != 0:
    print(f"Amount of tax: {tax}")
