# Find index of minimum value in array
def findMinIndex (arr, start, n):
	minIndex = start

	for i in range(start+1, n):
		if arr[i] < arr[minIndex]:
			minIndex = i

	return minIndex


def selectionSort(arr):
	n = len(arr)

	for i in range(n):
		minIndex = findMinIndex(arr, i, n)
		if i != minIndex:
			arr[i], arr[minIndex] = arr[minIndex], arr[i]

	return

##---------------------------------------------------------------------------##

# instead of helper function we use double for loop
def selectionSortSimple(arr):
	n = len(arr)

	for i in range(n-1):
		minIndex = i
		for j in range(i+1, n):
			if arr[j] < arr[minIndex]:
				minIndex = j
		if i != minIndex:
			arr[i], arr[minIndex] = arr[minIndex], arr[i]

	return


# test
arr = [5, 3, 0, 1, 4, 2]
print ("Original array:\t{}".format(arr))
selectionSortSimple(arr)
print ("Sorted array:\t{}".format(arr))
