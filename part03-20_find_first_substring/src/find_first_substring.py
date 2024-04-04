# Write your solution here
string = input("Please type in a word: ")
char = input("Please type in a character: ")

i = string.find(char)

# mammoth

if i != -1 and len(string) >= i + 3:
    print(string[i : i + 3])
