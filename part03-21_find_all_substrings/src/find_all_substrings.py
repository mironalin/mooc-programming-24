# Write your solution here
string = input("Please type in a word: ")
char = input("Please type in a character: ")

while string.find(char) != -1:
    i = string.find(char)

    # mammoth

    if i != -1 and len(string) >= i + 3:
        print(string[i : i + 3])
    string = string[i + 1 :]
