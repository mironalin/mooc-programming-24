# Write your solution here
def chessboard(length):
    it_1 = 0
    while it_1 < length:
        if it_1 % 2 == 0:
            str = "10" * length
        else:
            str = "01" * length

        print(str[0:length])
        it_1 += 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
