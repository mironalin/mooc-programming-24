# Write your solution here
letter_1 = input("1st letter: ")
letter_2 = input("2st letter: ")
letter_3 = input("3st letter: ")

letter_middle = ""

if letter_2 > letter_1 and letter_1 > letter_3:
    letter_middle = letter_1
elif letter_3 > letter_1 and letter_1 > letter_2:
    letter_middle = letter_1

elif letter_1 > letter_3 and letter_3 > letter_2:
    letter_middle = letter_3
elif letter_2 > letter_3 and letter_3 > letter_1:
    letter_middle = letter_3

elif letter_1 > letter_2 and letter_2 > letter_3:
    letter_middle = letter_2
elif letter_3 > letter_2 and letter_2 > letter_1:
    letter_middle = letter_2
print(f"The letter in the middle is {letter_middle}")
