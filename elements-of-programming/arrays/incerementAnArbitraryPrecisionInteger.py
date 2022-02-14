#  Write a program which takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.

def increment(numbers):
    carry = 1
    for i in range(len(numbers)-1, -1, -1):
        numbers[i] += carry
        if numbers[i] >= 10:
            numbers[i] -= 10
            carry = 1
        else:
            carry = 0
            break
    if carry == 1:
        numbers.insert(0, 1)
    print(numbers)

# write a another solution using with using string conversion
def incerement2(numbers):
    numbers = list(str(int(''.join(str(x) for x in numbers))+1))
    print(numbers)

incerement2([1,2,9])

# Certain applications require arbitrary precision arithmetic. One way to achieve this is to use arrays
# to represent integers, e.9., with one digit per array entry with the most significant digit appearing
# first, and a negative leading digit denoting a negative integer. For example, <1,9,3,7,0,7,7,2,1>
# represents 193707721 and (-7,6,1.,8,3,8,2,5,7,2,8,7> represents -761838257287.
# Write a program that takes two arrays representing integers, and retums an integer representing their product.
#  For example, since 193707721.x -761838257287 = -147573952589676412927, if
# the inputs are (1,9,3,7,0,7,7,2, 1) and <-7,6,L,8,3,8,2,5,7,2,8,7>, your function should refum
# (-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.

def multiplyTwoArbitraryPrecisionIntegers(number1, number2):
    number1str = ''.join(str(x) for x in number1)
    number2str = ''.join(str(x) for x in number2)
    result = int(number1str) * int(number2str)
    resultArray = []
    for i in str(result):
        resultArray.append(i)
    return resultArray

multiplyTwoArbitraryPrecisionIntegers([1,9], [-1, 0])



