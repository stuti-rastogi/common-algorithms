def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key

    return


# test
arr = [5, 3, 0, 1, 4, 2]
print ("Original array:\t{}".format(arr))
insertionSort(arr)
print ("Sorted array:\t{}".format(arr))
