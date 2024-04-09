# Write your solution here
def line(length, str):
    if str == "":
        str = "*"
    print(str[0] * length)
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")