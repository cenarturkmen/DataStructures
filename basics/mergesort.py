def mergeSort(arr):
    if len(arr)>1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                
            else:
                arr[k] = right[j] 
                j += 1
            k += 1
            
        while i<len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j<len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return  arr  

test_case1 = [58, 147, 12232, 1400000, 1231, 0]
test_case2 = [0,0,0,0,1,0,0]

print(mergeSort(test_case1), mergeSort(test_case2))



