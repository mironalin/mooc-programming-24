# Write your solution here
def length_of_longest(list):
    longest = list[0]
    for i in list:
        if len(i) > len(longest):
            longest = i
            
    return len(longest)