# Write your solution here
list = []
str = input("Word: ")

while str not in list:
    list.append(str)
    
    str = input("Word: ")
    
print(f"You typed in {len(list)} different words")