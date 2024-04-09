# Copy here code of line function from previous exercise and use it in your solution
def line(length, str):
    if str == "":
        str = "*"
    print(str[0] * length)
    
def shape(size, char_trg, height, char_sqr):
    it = 1
    while it <= size:
        line(it, char_trg)
        it += 1
    
    it = 0
    while it < height:
        line(size, char_sqr)
        it += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")