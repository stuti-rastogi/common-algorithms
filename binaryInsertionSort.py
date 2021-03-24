def binarySearch(arr, start, end, key):
    '''
        Return the position where in array
        key should be inserted
    '''
    if start == end:
        if arr[start] < key:
            return start + 1
        else:
            return start

    if start > end:
        return start

    mid = (start + end) // 2

    if key > arr[mid]:
        return binarySearch(arr, mid+1, end, key)
    elif key < arr[mid]:
        return binarySearch(arr, start, mid-1, key)
    else:
        return mid


def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        pos = binarySearch(arr, 0, i-1, key)
        arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]
    return arr


# test
arr = [5, 3, 0, 1, 4, 2]
print ("Original array:\t{}".format(arr))
arr = insertionSort(arr)
print ("Sorted array:\t{}".format(arr))
