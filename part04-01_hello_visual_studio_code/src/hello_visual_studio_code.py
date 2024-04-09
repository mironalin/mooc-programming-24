# Write your solution here
while True:
    string = input("Editor: ")
    string = string.lower()
    if string == "visual studio code":
        print("an excellent choice!")
        break
    
    if string == "notepad" or string == "word":
        print("awful")
    else:
        print("not good")