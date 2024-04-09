# Write your solution here
def spruce(size):
    print("a spruce!")
    it = 1
    while it <= size:
        print(" " * (size - it) + "*" * (it * 2 - 1))
        it += 1
    
    print(" " * (size - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)