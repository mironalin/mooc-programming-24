# Write your solution here
def most_common_character(str):
    most = 0
    for char in str:
        if str.count(char) > most:
            char_long = char
            most = str.count(char)

    return char_long