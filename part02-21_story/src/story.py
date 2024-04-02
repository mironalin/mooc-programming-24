# Write your solution here
story = ""
last = ""
while True:
    str = input("Please type in a word: ")

    if str == "end" or str == last:
        break

    last = str
    story += str + " "

print(story)
