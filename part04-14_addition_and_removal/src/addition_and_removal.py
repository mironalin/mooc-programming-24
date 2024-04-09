# Write your solution here
list = []
it = 1


print(f"The list is now {list}")
str = input("a(d)d, (r)emove or (e)xit: ")

while str != "x":
    if str == "d":
        list.append(it)
        it += 1
    elif str == "r":
        list.remove(it - 1)
        it -= 1
    
    print(f"The list is now {list}")
    str = input("a(d)d, (r)emove or (e)xit: ")
    
print("Bye!")