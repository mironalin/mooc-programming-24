# Write your solution here
number = int(input("Please type in a number: "))

i = 0

while i < number:
    if i == number - 1:
        print(number)
    else:
        print(i + 2)
        print(i + 1)

    i += 2
