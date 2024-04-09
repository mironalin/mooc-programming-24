# Write your solution here
def everything_reversed(list):
    new_list = [i[::-1] for i in list]
    new_list.reverse()
    return new_list
