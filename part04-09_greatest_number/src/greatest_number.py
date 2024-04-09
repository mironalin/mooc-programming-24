# Write your solution here
def greatest_number(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)