# Write your solution here

def distinct_numbers(list):
    new_list = []
    [new_list.append(x) for x in list if x not in new_list]
    
    return sorted(new_list)