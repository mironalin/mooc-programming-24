# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

count = 0
sum = 0
pos = 0
neg = 0
while True:
    number = int(input("Number: "))

    if number == 0:
        break
    count += 1
    sum += number
    if number > 0:
        pos += 1
    else:
        neg += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / count}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")
