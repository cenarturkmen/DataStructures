# This problem is concemed with deleting repeated elements from a sorted array. For example, for
# the array  <2,3,5,5,7,11,11,11,13> , then after deletion, the array is (2,3,5,7,11,13,0,0,0). After
# deleting repeated elements, there are 6 valid entries. There are no requirements as to the values
# stored beyond the last valid element.
# Write a program which takes as input a sorted array and updates it so that all duplicates have been
# removed and the remaining elements have been shifted left to fill the emptied indices. Return the
# number of valid elements. Many languages have library functions for performing this operation you cannot use these functions.

def deleteDuplicatesFromSortedArray(arr):
    c = 0
    for i in range(1, len(arr)-1):
        if arr[i] == arr[i-1]:

            arr[i] = 0
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
    print(arr)

deleteDuplicatesFromSortedArray([2,3,5,5,7,11,11,11,13])