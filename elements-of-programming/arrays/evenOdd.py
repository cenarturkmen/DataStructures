# : Your input is an array of  integers, and you have to reorder its entries so that the even entries appear first. 
# This is easy if you use O(n) space, where n is the length of the array. However, you are required to solve it without allocating additional storage

def evenOdd(numbers):
    start = 0
    end = len(numbers)
    while start<end :
        if(numbers[start] % 2 != 0):
            start += 1
        else:
            numbers[start], numbers[end] = numbers[end], numbers[start]
            end -= 1
