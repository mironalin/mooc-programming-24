# Write your solution here
def no_vowels(str: str):
    vowels = ["a", "e", "i", "o", "u"]
    for char in str:
        if char in vowels:
            str = str.replace(char, "")
    return str
