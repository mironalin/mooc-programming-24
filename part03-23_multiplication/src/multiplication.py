# Write your solution here
number = int(input("Please type in a number: "))
it_1 = 1

while it_1 <= number:
    it_2 = 1

    while it_2 <= number:
        print(f"{it_1} x {it_2} = {it_1 * it_2}")
        it_2 += 1

    it_1 += 1
