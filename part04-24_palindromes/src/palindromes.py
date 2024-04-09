# Write your solution here
def palindromes(str):
    return str == str[::-1]

str = input("Please type in a palindrome: ")
while not palindromes(str):
    str = input("Please type in a palindrome: ")
    print("that wasn't a palindrome")
    
print(f"{str} is a palindrome!")    
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
