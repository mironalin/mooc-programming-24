# Write your solution here
limit = int(input("Limit: "))
number = 1
sum = 1
str = "1"

while sum < limit:
    number += 1
    sum += number
    str += f" + {number}"

print(f"The consecutive sum: {str} = {sum}")
