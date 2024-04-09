# Copy here code of line function from previous exercise
def line(length, str):
    if str == "":
        str = "*"
    print(str[0] * length)
    
def triangle(size):
    # You should call function line here with proper parameters
    it = 1
    while it <= size:
        line(it, "#")
        it += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
