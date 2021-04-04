def countingSort(arr, k):
    '''
        Args:
            arr: Input array to be sorted
            k: Range of elements is [0,k]
        Return: 
            sortedArr: New sorted array
    '''
    n = len(arr)
    sortedArr = [0] * n
    counts = [0] * (k+1)                    # since 0 to k is (k+1) elements

    for i in range(n):
        counts[arr[i]] += 1

    for i in range(1, k+1):
        counts[i] = counts[i] + counts[i-1]

    for i in range(n-1, -1, -1):
        sortedArr[counts[arr[i]]-1] = arr[i]
        counts[arr[i]] -= 1

    return sortedArr


# test
arr = [5, 3, 0, 1, 4, 2]
print ("Original array:\t{}".format(arr))
sortedArr = countingSort(arr, max(arr))
print ("Sorted array:\t{}".format(sortedArr))
