# Write your solution here
word = input("Word: ")

space = (28 - len(word)) // 2

print("*" * 30)
if len(word) % 2 == 0:
    print("*" + " " * space + word + " " * space + "*")
else:
    print("*" + " " * space + word + " " * (space + 1) + "*")
print("*" * 30)
