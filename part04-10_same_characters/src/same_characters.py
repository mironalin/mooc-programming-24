# Write your solution here
def same_chars(str, index_1, index_2):
    if index_1 >= len(str) or index_2 >= len(str):
        return False
    
    return str[index_1] == str[index_2]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))