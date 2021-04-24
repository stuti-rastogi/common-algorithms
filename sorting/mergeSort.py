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


# Here we use sentinels to cover all elements
# instead of the two extra while loops at the end
# REFER CLRS # 31
def mergeSimple(arr, start, mid, end):
	sizeL = mid - start + 1
	sizeR = end - mid

	# +1 for the sentinels
	L = [0] * (sizeL + 1)
	R = [0] * (sizeR + 1)

	# copy elements from start to mid inclusive from arr to L
	for i in range(sizeL):
		L[i] = arr[start + i]

	# copy elements from mid+1 to end inclusive from arr to R
	for i in range(sizeR):
		R[i] = arr[mid + 1 + i]

	# sentinels
	L[sizeL] = float("inf")
	R[sizeR] = float("inf")

	i = 0; j = 0
	k = start

	# we know we are arranging the elements from start to end
	while k <= end:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1


def mergeSortHelper(arr, start, end):
	if start < end:
		mid = (start + end) // 2
		mergeSortHelper(arr, start, mid)
		mergeSortHelper(arr, mid+1, end)
		mergeSimple(arr, start, mid, end)


def mergeSort(arr):
	n = len(arr)
	# call recursive function with start and end
	mergeSortHelper(arr, 0, n-1)


# test
arr = [5, 3, 0, 1, 4, 2]
print ("Original array:\t{}".format(arr))
mergeSort(arr)
print ("Sorted array:\t{}".format(arr))
