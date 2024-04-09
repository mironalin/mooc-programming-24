# Write your solution here

def shortest(list):
    shortest = list[0]
    
    for i in list:
        if len(shortest) > len(i):
            shortest = i
        
    return shortest