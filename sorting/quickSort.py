def partition(arr, p, r):
    x = arr[r]
    i = p-1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return (i+1)


def quickSortHelper(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSortHelper(arr, p, q-1)
        quickSortHelper(arr, q+1, r)


def quickSort(arr):
    n = len(arr)
    # call recursive function with start and end
    quickSortHelper(arr, 0, n-1)


# test
arr = [5, 3, 0, 1, 4, 2]
print ("Original array:\t{}".format(arr))
quickSort(arr)
print ("Sorted array:\t{}".format(arr))
