# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index_1 = string.find(substring)
index_2 = -1

if index_1 != -1:
    index_2 = string.find(substring, index_1 + len(substring))

if index_2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index_2}.")
