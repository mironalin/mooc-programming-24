# Write your solution here
string = input("Please type in a string: ")

i = -1
sum = ""

while i >= -len(string):
    sum = string[i] + sum
    print(sum)
    i -= 1
