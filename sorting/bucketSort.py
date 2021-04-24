from insertionSort import insertionSort

def bucketSort(arr):
	numSlots = 10
	buckets = []

	for i in range(numSlots):
		buckets.append([])

	for x in arr:
		buckets[int(x * numSlots)].append(x)

	for bucket in buckets:
		insertionSort(bucket)

	sortedArr = []
	for bucket in buckets:
		for x in bucket:
			sortedArr.append(x)

	return sortedArr

if __name__ == "__main__":
	# test
	arr = [0.572, 0.284, 0.265, 0.51, 0.423, 0.05, 0.444, 0.112, 0.157, 0.14, 0.951, 0.273, 0.555, 0.904, 0.058]
	print ("Original array:\t{}".format(arr))
	sortedArr = bucketSort(arr)
	print ("Sorted array:\t{}".format(sortedArr))
