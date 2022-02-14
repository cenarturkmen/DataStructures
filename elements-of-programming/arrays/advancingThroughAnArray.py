# in a particular board garne, a player has to try to advance through a sequence of positions. Each
# position has a nonnegative integer associated with it, representing the maximum you can advance
# from that position in one move. You begin at the first position, and win by getting to the last
# position. For example,let A = (3,3,1.,0,2,0,1) represent the board garr.e, i.e., the lth entry in A is
# the maximum we can advance from L Then the game can be won by the following sequence of
# advances through A: take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from
# A[ ]toA[6],whichisthelastPosition.NotethatA[0] =3>1,,4[1] =3)3,andA[4] =2>2,soall
# moves are valid. If A instead was (3, 2,0,0,2,0,1), it would not possible to advance past position 3,
# so the game cannot be won.

# Write a program which takes an array of n integers, where A[i] denotes the maximum you can
# advance from index l, and retums whether it is possible to advance to the last index starting from
# the beginning of the array.



def advancingThroughAnArray(arr):
    start = 0
    end = len(arr) - 1
    i = 0

    while i<= start and start<end:
        start = max(start, arr[i]+i)
        i += 1
    return start>=end

print(advancingThroughAnArray([3,3,7,0,2,0,1, 3]))
