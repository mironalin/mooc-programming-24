# Write your solution here
sentence = input("Please type in a sentence: ")
it_1 = 0

if len(sentence) != 0:
    print(sentence[0])
    while it_1 < len(sentence):
        if sentence[it_1] == " ":
            print(sentence[it_1 + 1])
        it_1 += 1
