# Copy here code of line function from previous exercise
def line(length, str):
    if str == "":
        str = "*"
    print(str[0] * length)
    
def square(size, character):
    # You should call function line here with proper parameters
    it = 0
    while it < size:
        line(size, character)
        it += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")