# Write your solution here
list = []

num = int(input("How many items: "))
it = 1

while it <= num:
    list.append(int(input(f"Item {it}: ")))
    it += 1
    
print(list)