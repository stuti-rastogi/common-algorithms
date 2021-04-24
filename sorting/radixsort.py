def countingSort(arr, exp):
	'''
		Args:
			arr: Input array to be sorted
			exp: 10^d when the dth digit is being processed
		NOTE:
			- No return, we copy output back to arr
			- k is not an argument since it is fixed for decimal
	'''
	k = 9                                   # range is [0,9] for decimal digits
	n = len(arr)
	sortedArr = [0] * n
	counts = [0] * (k+1)                    # since 0 to k is (k+1) elements

	# at the end of this loop, counts[i] holds the number of elements in arr
	# where the dth digit is i (exp = 10^d)
	for i in range(n):
		digit = (arr[i]//exp) % 10
		counts[digit] += 1

	# at the end of this loop, counts[i] holds the number of elemenets with dth
	# digit <= i
	for i in range(1, k+1):
		counts[i] = counts[i] + counts[i-1]

	# add elements to sortedArr as per position computed in counts
	for i in range(n-1, -1, -1):
		digit = (arr[i]//exp) % 10
		sortedArr[counts[digit]-1] = arr[i]
		counts[digit] -= 1

	# copy sortedArr back to arr
	for i in range (n):
		arr[i] = sortedArr[i]


def radixSort(arr):
	# We take only the array as input hence
	# we need to calculate max number of digits
	maxVal = max(arr)

	# exp is 10^i for i from 0 to d
	exp = 1
	while (maxVal//exp) > 0:
		countingSort(arr, exp)
		exp *= 10

# test
arr = [5724, 354, 1000, 2568, 7933, 5621]
print ("Original array:\t{}".format(arr))
radixSort(arr)
print ("Sorted array:\t{}".format(arr))
