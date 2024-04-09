# Write your solution here

def all_the_longest(list):
    longest_list = []
    longest = list[0]
    for i in list:
        if len(i) >= len(longest):
            longest = i
            
    for i in list:
        if len(i) == len(longest):
            longest_list.append(i)
            
    return longest_list
