# Write your solution here
def squared(str, length):
    str = str * length * length
    it = 0
    start = 0
    end = length
    while it < length:

        print(str[start:end])

        start += length
        end += length

        it += 1
