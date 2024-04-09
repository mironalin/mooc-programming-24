# Write your solution here
def longest_series_of_neighbours(list):
    longest = 1
    res = 1
    
    for i in range(1, len(list)):
        if abs(list[i - 1] - list[i]) == 1:
            res += 1
        else:
            res = 1

        longest = max(longest, res)
    
    return longest
