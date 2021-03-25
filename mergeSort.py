def merge(arr, start, mid, end):
    temp = [0] * (end - start + 1)

    i = start
    j = mid + 1
    k = 0

    while (i <= mid) and (j <= end):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(start, end+1):
        arr[i] = temp[i - start]


def mergeSortHelper(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSortHelper(arr, start, mid)
        mergeSortHelper(arr, mid+1, end)
        merge(arr, start, mid, end)


def mergeSort(arr):
    n = len(arr)
    # call recursive function with start and end
    mergeSortHelper(arr, 0, n-1)


# test
arr = [5, 3, 0, 1, 4, 2]
print ("Original array:\t{}".format(arr))
mergeSort(arr)
print ("Sorted array:\t{}".format(arr))
